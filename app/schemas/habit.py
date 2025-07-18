from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.core.enums import PeriodEnum


class HabitBaseSchema(BaseModel):
    title: str
    description: Optional[str] = None
    periodicity: PeriodEnum = PeriodEnum.DAILY
    reminder_time: Optional[str] = None


class HabitCreateSchema(HabitBaseSchema):
    is_active: Optional[bool] = True

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Drink water",
                "description": "Drink at least 2 liters of water",
                "periodicity": "daily",
                "reminder_time": "08:00",
                "is_active": True,
            }
        }


class HabitReadSchema(HabitBaseSchema):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Drink water",
                "description": "Drink at least 2 liters of water",
                "periodicity": "daily",
                "reminder_time": "08:00",
                "is_active": True,
                "created_at": "2025-07-09T10:00:00",
                "updated_at": "2025-07-09T12:00:00",
            }
        }


class HabitUpdateSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    periodicity: Optional[PeriodEnum] = None
    reminder_time: Optional[str] = None
    is_active: Optional[bool] = None

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Drink water",
                "description": "Drink at least 2 liters of water",
                "periodicity": "weekly",
                "reminder_time": "09:00",
                "is_active": False,
            }
        }
