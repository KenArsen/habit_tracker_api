from fastapi import HTTPException, Response

from app.api.deps import CurrentUserDep
from app.core.config import settings
from app.core.security import auth, hash_password, verify_password
from app.crud import user as user_crud
from app.schemas.auth import ChangePasswordSchema, LoginSchema
from app.services.user import UserService


class AuthService(UserService):
    async def login(self, data: LoginSchema, response: Response):
        user = await user_crud.get_by_email(self.db, data.email)
        if not user or not verify_password(data.password, user.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        access_token = auth.create_access_token(uid=user.email)
        response.set_cookie(settings.JWT_ACCESS_COOKIE_NAME, access_token)
        return {"access_token": access_token}

    async def change_password(self, data: ChangePasswordSchema, current_user: CurrentUserDep):
        user = await user_crud.get_by_id(self.db, current_user.id)
        if not verify_password(data.old_password, user.password):
            raise HTTPException(status_code=401, detail="Invalid current password")

        user.password = hash_password(data.new_password)

        await self.db.commit()
        return {"detail": "Password updated successfully"}
