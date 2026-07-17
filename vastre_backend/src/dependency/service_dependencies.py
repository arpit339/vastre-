from fastapi import Depends

from src.dependency.repository_dependencies import get_otp_repository, get_user_repository
from src.repository.otp_repository import OtpRepository
from src.repository.user_repository import UserRepository
from src.service.otp_service import OtpService
from src.service.user_service import UserService


def get_otp_service(otp_repo: OtpRepository=Depends(get_otp_repository)):
    return OtpService(otp_repo)

def get_user_service(user_repo: UserRepository=Depends(get_user_repository)):
    return UserService(user_repo)