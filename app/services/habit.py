from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import habit as habit_crud
from app.models.habit import Habit
from app.schemas.habit import HabitCreateSchema, HabitUpdateSchema


class HabitService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id_or_404(self, habit_id: int, user_id: int) -> Habit:
        habit = await habit_crud.get_by_id(self.db, habit_id, user_id)
        if not habit:
            raise HTTPException(status_code=404, detail="Habit not found")
        return habit

    async def list(self, user_id: int) -> list[Habit]:
        return await habit_crud.get_all(self.db, user_id)

    async def create(self, data: HabitCreateSchema, user_id: int) -> Habit:
        habit = Habit(**data.model_dump(), user_id=user_id)
        return await habit_crud.create(self.db, habit)

    async def update(self, habit_id: int, user_id: int, data: HabitUpdateSchema) -> Habit:
        habit = await self.get_by_id_or_404(habit_id, user_id)
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(habit, key, value)
        return await habit_crud.update(self.db, habit)

    async def delete(self, habit_id: int, user_id: int):
        habit = await self.get_by_id_or_404(habit_id, user_id)
        await habit_crud.delete(self.db, habit)
