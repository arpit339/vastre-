import datetime
from datetime import timedelta

from src.model.userModel import UserModel
from src.model.otp_model import OtpModel
from src.exception.resource_not_found_error import ResourceNotFound
from src.utils.email_util import generate_otp

from src.utils.argon_hash import hash_otp
from src.utils.argon_hash import verify_otp


class OtpService:

    def __init__(self, session):
        self.session = session

    async def get_user(self, email):
        db_user = await self.session.get_user(email)
        otp = generate_otp(email)

        if otp:
            await self.session.delete_otp(email)
            otp_user = OtpModel(email=email, otp_code=hash_otp(otp), expires_at=datetime.datetime.now() + timedelta(minutes=10))
            await self.session.save_otp(otp_user)
            await self.session.increment_attempts(otp_user)
            return None
        else:
            return {"wrong email"}

    async def verify_otp(self, email, otp_code, user_name=None, contact=None):
        db_otp = await self.session.get_latest_otp(email)

        if not db_otp:
            return {"message": "wrong email"}

        if db_otp.expires_at < datetime.datetime.now():
            await self.session.delete_otp(email)
            return {"message": "otp expired"}

        if db_otp.attempts >= 5:
            return {"message": "too many attempts, request a new otp"}

        if not verify_otp( db_otp.otp_code , otp_code):
            return {"message": "invalid otp"}

        db_otp.is_verified = True
        await self.session.delete_otp(email)

        db_user = await self.session.get_user(email)

        if db_user:
            return {"message": "login success", "user_id": db_user.user_id}

        new_user = UserModel(email=email, user_name=user_name, contact=contact, is_verified=True)
        new_user = await self.session.user_repo.save(new_user)
        login_new_user = await self.session.get_user(new_user.email)
        if login_new_user:
            return {"message": "login success", "user_id": login_new_user.user_id}
        return {"message": "signup success", "user_id": new_user.user_id}

