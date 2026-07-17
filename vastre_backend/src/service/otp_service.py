from src.exception.resource_not_found_error import ResourceNotFound
from src.utils.email_util import generate_otp


class OtpService:

    def __init__(self,session):
        self.session = session

    async def get_user(self,email):
        db_user = await self.session.get_user(email)
        otp = generate_otp(email)
        print(otp)
        return db_user

