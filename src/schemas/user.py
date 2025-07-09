from pydantic import BaseModel, EmailStr


class UserBaseSchema(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str


class UserSchema(UserBaseSchema):
    id: int


class RegisterSchema(UserBaseSchema):
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


class LoginSchema(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "arsen.kenjegulov.bj@gmail.com",
                "password": "arsen2002",
            }
        }


class MeSchema(UserBaseSchema):
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
