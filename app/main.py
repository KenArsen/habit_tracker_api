from fastapi import FastAPI

from app.api.v1.api import main_router

app = FastAPI(summary="Habit tracker API")

app.include_router(main_router)
