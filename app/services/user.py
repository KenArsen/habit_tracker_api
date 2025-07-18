from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import NotFoundException, UserAlreadyExistsException
from app.core.security import hash_password
from app.crud import user as user_crud
from app.models import User
from app.schemas.auth import RegisterSchema
from app.schemas.user import UserUpdateSchema


class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id_or_404(self, user_id: int) -> User:
        user = await user_crud.get_by_id(self.db, user_id)
        if not user:
            raise NotFoundException("User")
        return user

    async def create(self, data: RegisterSchema) -> User:
        existing_user = await user_crud.get_by_email(self.db, data.email)
        if existing_user:
            raise UserAlreadyExistsException()

        user = User(**data.model_dump())
        user.password = hash_password(data.password)
        return await user_crud.create(self.db, user)

    async def update(self, user_id: int, data: UserUpdateSchema) -> User:
        user = await self.get_by_id_or_404(user_id)
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(user, key, value)
        return await user_crud.update(self.db, user)

    async def delete(self, user_id: int):
        user = await self.get_by_id_or_404(user_id)
        await user_crud.delete(self.db, user)
