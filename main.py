import uvicorn
from fastapi import FastAPI

from src.api import main_router

app = FastAPI(summary="Habit tracker API")

app.include_router(main_router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
