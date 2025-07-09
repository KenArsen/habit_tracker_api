from fastapi import APIRouter

from src.api.users import router as user_router

main_router = APIRouter()
main_router.include_router(user_router, tags=["users"])
