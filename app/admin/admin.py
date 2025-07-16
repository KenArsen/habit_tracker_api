from sqladmin import Admin

from app.admin.views import HabitAdmin, UserAdmin
from app.core.database import engine


def setup_admin(app):
    admin = Admin(
        app,
        engine,
        title="Habit Tracker Admin",
        base_url="/admin",
    )
    admin.add_view(UserAdmin)
    admin.add_view(HabitAdmin)
