from typing import List

from fastapi import APIRouter

from app.api.deps import CurrentUserDep, SessionDep
from app.schemas.habit import HabitCreateSchema, HabitReadSchema, HabitUpdateSchema
from app.services.habit import HabitService

router = APIRouter()


@router.get("", response_model=List[HabitReadSchema])
async def list_habits(session: SessionDep, current_user: CurrentUserDep):
    service = HabitService(session)
    return await service.list(current_user.id)


@router.post("", response_model=HabitReadSchema)
async def create_habit(data: HabitCreateSchema, session: SessionDep, current_user: CurrentUserDep):
    service = HabitService(session)
    return await service.create(data, current_user.id)


@router.get("/{pk}", response_model=HabitReadSchema)
async def get_habit(pk: int, session: SessionDep, current_user: CurrentUserDep):
    service = HabitService(session)
    return await service.get_by_id_or_404(pk, current_user.id)


@router.put("/{pk}", response_model=HabitReadSchema)
@router.patch("/{pk}", response_model=HabitReadSchema)
async def update_habit(pk: int, data: HabitUpdateSchema, session: SessionDep, current_user: CurrentUserDep):
    service = HabitService(session)
    return await service.update(pk, current_user.id, data)


@router.delete("/{pk}", status_code=204)
async def delete_habit(pk: int, session: SessionDep, current_user: CurrentUserDep):
    service = HabitService(session)
    await service.delete(pk, current_user.id)
