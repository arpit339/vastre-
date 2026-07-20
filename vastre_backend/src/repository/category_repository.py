from src.model.category_model import CategoryModel
from sqlalchemy import select
class CategoryRepo():
    def __init__(self,session):
        self.session = session

    async def add_category(self, category:CategoryModel):
        self.session.add(category)
        await self.session.flush()
        await self.session.refresh(category)
        return category
    
    async def get_category_by_id(self, category_id):
        result =await self.session.get(CategoryModel,category_id)
        return result

    async def get_all_category(self):
        stmt = select(CategoryModel)
        result = await self.session.execute(stmt)
        return result.scalars().all()