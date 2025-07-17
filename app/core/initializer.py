from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin

from app.admin.views import HabitAdmin, UserAdmin
from app.core.config import settings
from app.core.database import engine


class AppInitializer:
    def __init__(self, app: FastAPI):
        self.app = app

    def setup(self):
        self._setup_cors()
        self._setup_admin()

    def _setup_cors(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=settings.CORS_ORIGINS,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def _setup_admin(self):
        admin = Admin(
            app=self.app,
            engine=engine,
            title="Habit Tracker Admin",
            base_url="/admin",
        )
        admin.add_view(UserAdmin)
        admin.add_view(HabitAdmin)
