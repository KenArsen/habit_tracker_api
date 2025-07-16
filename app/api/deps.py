from typing import Annotated

from fastapi import Depends, HTTPException, Request
from jose import JWTError, jwt
from sqlalchemy import select

from app.core.config import settings
from app.core.deps import SessionDep
from app.models import User


async def get_current_user(request: Request, session: SessionDep) -> User:
    token = request.cookies.get(settings.JWT_ACCESS_COOKIE_NAME)

    if not token:
        raise HTTPException(status_code=401, detail="Access token missing")

    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token payload")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    result = await session.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    return user


CurrentUserDep = Annotated[User, Depends(get_current_user)]
