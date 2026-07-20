from src.repository.category_repository import CategoryRepo
from src.schema.category_schema import CategoryRequest
from src.model.category_model import CategoryModel
from fastapi import UploadFile,Form
from src.service.cloudinary_service import upload_image, destroy_image,update_image
class CategoryService():
    def __init__(self,category_repo : CategoryRepo):
        self.category_repo = category_repo

    async def get_all_category(self):
        return await self.category_repo.get_all_category()
    
    async def add_category(self,category_name : str , image :UploadFile ):
        image_data = await upload_image(image)
        category = CategoryModel(category_name = category_name, slug= "category-" + category_name,category_image_url = image_data["url"],category_public_id = image_data["public_id"])
        return await self.category_repo.add_category(category)
    
    async def update_category(self, category_id :int,category_name :str , image:UploadFile ):
        dbCategory = await self.category_repo.get_category_by_id(category_id)
        if dbCategory.category_public_id:
            result = await update_image(image,dbCategory.category_public_id)
            dbCategory.catgory_name = category_name
            dbCategory.slug = "category-"+category_name
            dbCategory.category_image_url = result["url"]
        return dbCategory
    
    async def get_category_by_id(self,category_id: int):
        return await self.category_repo.get_category_by_id(category_id)