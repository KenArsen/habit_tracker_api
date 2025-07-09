from authx import AuthX, AuthXConfig
from passlib.context import CryptContext

from src.core.config import settings

config = AuthXConfig(
    JWT_ALGORITHM=settings.JWT_ALGORITHM,
    JWT_SECRET_KEY=settings.JWT_SECRET_KEY,
    JWT_TOKEN_LOCATION=settings.JWT_TOKEN_LOCATION,
    JWT_ACCESS_COOKIE_NAME=settings.JWT_ACCESS_COOKIE_NAME,
)

auth = AuthX(config=config)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
