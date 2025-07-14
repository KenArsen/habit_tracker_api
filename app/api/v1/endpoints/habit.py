from fastapi import APIRouter
from sqlalchemy import select

from app.api.deps import CurrentUserDep, SessionDep
from app.models.habit import Habit
from app.schemas.habit import HabitCreateSchema, HabitReadSchema

router = APIRouter()


@router.post("", response_model=HabitReadSchema)
async def create_habit(data: HabitCreateSchema, session: SessionDep, current_user: CurrentUserDep):
    habit = Habit(**data.model_dump(), user_id=current_user.id)
    session.add(habit)
    await session.commit()
    await session.refresh(habit)
    return habit


@router.get("", response_model=list[HabitReadSchema])
async def list_habits(session: SessionDep, current_user: CurrentUserDep):
    result = await session.execute(select(Habit).where(Habit.user_id == current_user.id))
    return result.scalars().all()
