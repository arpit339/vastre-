from fastapi.params import Depends
from sqlalchemy import delete, select

from src.model.otp_model import OtpModel
from src.repository.user_repository import UserRepository


class OtpRepository:

    def __init__(self, session, user_repo: UserRepository):
        self.session = session
        self.user_repo = user_repo

    async def get_user(self, email):
        return await self.user_repo.get_user_by_email(email)

    async def save_otp(self, otp_user: OtpModel):
        self.session.add(otp_user)
        await self.session.flush()
        await self.session.refresh(otp_user)
        return otp_user

    async def get_latest_otp(self, email: str):
        statement = (
            select(OtpModel)
            .where(OtpModel.email == email)
            .order_by(OtpModel.expires_at.desc())
        )
        result = await self.session.execute(statement)
        return result.scalars().first()

    async def delete_otp(self, email: str):
        statement = delete(OtpModel).where(OtpModel.email == email)
        await self.session.execute(statement)

    @staticmethod
    async def increment_attempts(otp_user: OtpModel):
        otp_user.attempts += 1
        return otp_user.attempts



