from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.habit import Habit


class HabitRepository:
    @staticmethod
    async def get_by_id(session: AsyncSession, habit_id: int, user_id: int) -> Habit | None:
        result = await session.execute(select(Habit).where(Habit.id == habit_id, Habit.user_id == user_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def get_all(session: AsyncSession, user_id: int) -> Sequence[Habit]:
        result = await session.execute(select(Habit).where(Habit.user_id == user_id))
        return result.scalars().all()

    @staticmethod
    async def create(session: AsyncSession, habit: Habit) -> Habit:
        session.add(habit)
        await session.commit()
        await session.refresh(habit)
        return habit

    @staticmethod
    async def update(session: AsyncSession, habit: Habit) -> Habit:
        await session.commit()
        await session.refresh(habit)
        return habit

    @staticmethod
    async def delete(session: AsyncSession, habit: Habit) -> None:
        await session.delete(habit)
        await session.commit()
