from fastapi.params import Depends

from src.repository.user_repository import UserRepository


class OtpRepository:

    def __init__(self,session,user_repo : UserRepository):
        self.session = session
        self.user_repo = user_repo

    async def get_user(self,email):
        return await self.user_repo.get_user_by_email(email)