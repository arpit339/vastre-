from sqlalchemy import select

from src.model.userModel import UserModel


class UserRepository:
    def __init__(self,session):
        self.session = session


    async def get_user_by_email(self , email:str):
        statement = select(UserModel).where(UserModel.email == email)
        result = await self.session.execute(statement)
        return result.scalar_one_or_none()

    async def save(self,user:UserModel):
        self.session.add(user)
        await self.session.flush()
        await self.session.refresh(user)
        return user