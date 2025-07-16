from fastapi import APIRouter, Response, status

from app.api.deps import CurrentUserDep
from app.core.deps import SessionDep
from app.schemas.auth import ChangePasswordSchema, LoginSchema, MeSchema, RegisterSchema
from app.services.auth import AuthService

router = APIRouter()


@router.post("/register", response_model=MeSchema, status_code=status.HTTP_201_CREATED)
async def register(data: RegisterSchema, session: SessionDep):
    service = AuthService(db=session)
    return await service.create(data)


@router.post("/login")
async def login(data: LoginSchema, session: SessionDep, response: Response):
    service = AuthService(db=session)
    return await service.login(data=data, response=response)


@router.get("/me", response_model=MeSchema)
async def get_me(current_user: CurrentUserDep):
    return current_user


@router.post("/change-password", status_code=status.HTTP_200_OK)
async def change_password(current_user: CurrentUserDep, data: ChangePasswordSchema, session: SessionDep):
    service = AuthService(db=session)
    return await service.change_password(data=data, current_user=current_user)
