from pydantic import BaseModel, EmailStr


class UserBaseSchema(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str


class UserUpdateSchema(UserBaseSchema):
    class Config:
        json_schema_extra = {
            "example": {
                "email": "arsen.kenjegulov.bj@gmail.com",
                "first_name": "Arsen",
                "last_name": "Kenzhegulov",
            }
        }
