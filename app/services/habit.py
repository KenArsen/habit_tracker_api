from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import NotFoundException
from app.crud.habit import HabitRepository
from app.models.habit import Habit
from app.schemas.habit import HabitCreateSchema, HabitUpdateSchema


class HabitService:
    def __init__(self, db: AsyncSession, repository=HabitRepository()):
        self.db = db
        self.repository = repository

    async def get_by_id_or_404(self, habit_id: int, user_id: int) -> Habit:
        habit = await self.repository.get_by_id(self.db, habit_id, user_id)
        if not habit:
            raise NotFoundException("Habit")
        return habit

    async def list(self, user_id: int) -> Sequence[Habit]:
        return await self.repository.get_all(self.db, user_id)

    async def create(self, data: HabitCreateSchema, user_id: int) -> Habit:
        habit = Habit(**data.model_dump(), user_id=user_id)
        return await self.repository.create(self.db, habit)

    async def update(self, habit_id: int, user_id: int, data: HabitUpdateSchema) -> Habit:
        habit = await self.get_by_id_or_404(habit_id, user_id)
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(habit, key, value)
        return await self.repository.update(self.db, habit)

    async def delete(self, habit_id: int, user_id: int):
        habit = await self.get_by_id_or_404(habit_id, user_id)
        await self.repository.delete(self.db, habit)
