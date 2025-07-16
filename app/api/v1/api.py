from fastapi import APIRouter

from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.habit import router as habit_router

main_router = APIRouter()

main_router.include_router(auth_router, prefix="/auth", tags=["Auth"])
main_router.include_router(habit_router, prefix="/habit", tags=["Habit"])
