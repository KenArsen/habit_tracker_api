from pydantic import BaseModel, EmailStr, Field


class AuthBaseSchema(BaseModel):
    email: EmailStr
    first_name: str = Field(min_length=1, max_length=50)
    last_name: str = Field(min_length=1, max_length=50)


class LoginSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=50)

    class Config:
        json_schema_extra = {
            "example": {
                "email": "arsen.kenjegulov.bj@gmail.com",
                "password": "arsen2002",
            }
        }


class RegisterSchema(AuthBaseSchema):
    password: str = Field(min_length=8, max_length=50)

    class Config:
        json_schema_extra = {
            "example": {
                "email": "arsen.kenjegulov.bj@gmail.com",
                "first_name": "Arsen",
                "last_name": "Kenzhegulov",
                "password": "arsen2002",
            }
        }


class MeSchema(AuthBaseSchema):
    id: int

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "email": "arsen.kenjegulov.bj@gmail.com",
                "first_name": "Arsen",
                "last_name": "Kenzhegulov",
            }
        }


class ChangePasswordSchema(BaseModel):
    old_password: str = Field(min_length=8, max_length=50)
    new_password: str = Field(min_length=8, max_length=50)

    class Config:
        json_schema_extra = {
            "example": {
                "old_password": "arsen2002",
                "new_password": "2002arsen",
            }
        }
