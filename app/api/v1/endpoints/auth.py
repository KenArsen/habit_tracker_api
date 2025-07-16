from fastapi import APIRouter, HTTPException, Response, status
from sqlalchemy import select

from app.api.deps import CurrentUserDep
from app.core.config import settings
from app.core.deps import SessionDep
from app.core.security import auth, hash_password, verify_password
from app.models import User
from app.schemas.auth import ChangePasswordSchema, LoginSchema, MeSchema, RegisterSchema

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(data: RegisterSchema, session: SessionDep):
    result = await session.execute(select(User).filter(User.email == data.email))
    existing_user = result.scalar_one_or_none()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(
        email=data.email,
        first_name=data.first_name,
        last_name=data.last_name,
        password=hash_password(data.password),
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


@router.post("/login")
async def login(data: LoginSchema, session: SessionDep, response: Response):
    result = await session.execute(select(User).filter(User.email == data.email))
    user = result.scalar_one_or_none()
    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = auth.create_access_token(uid=user.email)
    response.set_cookie(settings.JWT_ACCESS_COOKIE_NAME, access_token)
    return {"access_token": access_token}


@router.get("/me", response_model=MeSchema)
async def get_me(current_user: CurrentUserDep):
    return current_user


@router.post("/change-password", status_code=status.HTTP_200_OK)
async def change_password(current_user: CurrentUserDep, data: ChangePasswordSchema, session: SessionDep):
    result = await session.execute(select(User).where(User.id == current_user.id))
    user: User = result.scalar_one_or_none()

    if not verify_password(data.old_password, user.password):
        raise HTTPException(status_code=401, detail="Invalid current password")

    user.password = hash_password(data.new_password)

    await session.commit()
    return {"detail": "Password updated successfully"}
