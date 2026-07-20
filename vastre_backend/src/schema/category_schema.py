from pydantic import BaseModel

class CategoryResponse(BaseModel):
    category_name : str

class CategoryRequest(BaseModel):
    category_name : str
    slug : str
    category_image_url : str
    category_public_id : str