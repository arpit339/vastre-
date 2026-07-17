from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.db_config import get_session
from src.repository.otp_repository import OtpRepository
from src.repository.user_repository import UserRepository


def get_user_repository(session: AsyncSession=Depends(get_session)):
    return UserRepository(session)

def get_otp_repository(session: AsyncSession=Depends(get_session), user_repo: UserRepository=Depends(get_user_repository)):
    return OtpRepository(session, user_repo)