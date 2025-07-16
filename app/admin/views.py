from sqladmin import ModelView

from app.models.habit import Habit
from app.models.user import User


class UserAdmin(ModelView, model=User):
    column_list = [
        User.id,
        User.email,
        User.first_name,
        User.last_name,
        User.created_at,
    ]
    column_searchable_list = [
        User.email,
        User.first_name,
        User.last_name,
    ]
    column_sortable_list = [User.created_at, User.first_name]
    form_excluded_columns = [User.password]
    column_labels = {
        User.email: "Email",
        User.first_name: "First Name",
        User.last_name: "Last Name",
        User.created_at: "Created At",
        User.updated_at: "Updated At",
        User.password: "Password",
    }
    page_size = 20


class HabitAdmin(ModelView, model=Habit):
    column_list = [
        Habit.id,
        Habit.title,
        Habit.description,
        Habit.user_id,
        Habit.created_at,
    ]
    column_searchable_list = [Habit.title]
    column_sortable_list = [Habit.created_at]
    column_labels = {
        Habit.title: "Title",
        Habit.description: "Description",
        Habit.user_id: "User",
        Habit.created_at: "Created At",
        Habit.updated_at: "Updated At",
    }
    page_size = 20
