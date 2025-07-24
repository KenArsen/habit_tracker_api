from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import NotFoundException, UserAlreadyExistsException
from app.core.security import hash_password
from app.crud.user import UserRepository
from app.models import User
from app.schemas.auth import RegisterSchema
from app.schemas.user import UserUpdateSchema


class UserService:
    def __init__(self, db: AsyncSession, repository=UserRepository()):
        self.db = db
        self.repository = repository

    async def get_by_id_or_404(self, user_id: int) -> User:
        user = await self.repository.get_by_id(self.db, user_id)
        if not user:
            raise NotFoundException("User")
        return user

    async def create(self, data: RegisterSchema) -> User:
        existing_user = await self.repository.get_by_email(self.db, data.email)
        if existing_user:
            raise UserAlreadyExistsException()

        user = User(**data.model_dump())
        user.password = hash_password(data.password)
        return await self.repository.create(self.db, user)

    async def update(self, user_id: int, data: UserUpdateSchema) -> User:
        user = await self.get_by_id_or_404(user_id)
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(user, key, value)
        return await self.repository.update(self.db, user)

    async def delete(self, user_id: int):
        user = await self.get_by_id_or_404(user_id)
        await self.repository.delete(self.db, user)
