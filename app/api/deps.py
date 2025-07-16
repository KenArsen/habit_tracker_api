from typing import Annotated

from fastapi import Depends, Request
from jose import JWTError, jwt
from sqlalchemy import select

from app.core.config import settings
from app.core.deps import SessionDep
from app.core.exceptions import (
    AccessTokenMissingException,
    InvalidTokenException,
    InvalidTokenPayloadException,
    NotFoundException,
)
from app.models import User


async def get_current_user(request: Request, session: SessionDep) -> User:
    token = request.cookies.get(settings.JWT_ACCESS_COOKIE_NAME)

    if not token:
        raise AccessTokenMissingException()

    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise InvalidTokenPayloadException()
    except JWTError:
        raise InvalidTokenException()

    result = await session.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()

    if user is None:
        raise NotFoundException("User")

    return user


CurrentUserDep = Annotated[User, Depends(get_current_user)]
