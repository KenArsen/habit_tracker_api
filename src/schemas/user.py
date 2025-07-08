from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBaseSchema(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str


class UserReadSchema(UserBaseSchema):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "email": "arsen.kenjegulov.bj@gmail.com",
                "first_name": "Arsen",
                "last_name": "Kenzhegulov",
                "created_at": "2025-07-08T14:35:22.000Z",
                "updated_at": "2025-07-08T14:40:10.000Z",
            }
        }


class UserCreateSchema(UserBaseSchema):
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "arsen.kenjegulov.bj@gmail.com",
                "first_name": "Arsen",
                "last_name": "Kenzhegulov",
                "password": "arsen2002",
            }
        }


class UserUpdateSchema(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "first_name": "Arsen",
                "last_name": "Kenzhegulov",
            }
        }
