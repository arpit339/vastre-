from fastapi.routing import APIRouter
from src.dependency.service_dependencies import get_category_service
from fastapi import status,Depends, UploadFile,Form
from src.schema.category_schema import CategoryRequest
from src.service.category_service import CategoryService
from fastapi.responses import FileResponse
categoryRouter = APIRouter(prefix="/category",tags=["category"])

@categoryRouter.post("/add",status_code=status.HTTP_201_CREATED)
async def add_category(category_name:str= Form(...),image :UploadFile= Form(...) , category_service : CategoryService = Depends(get_category_service)) :
    return await category_service.add_category(category_name, image)

@categoryRouter.get("/get/{category_id}",status_code=status.HTTP_200_OK)
async def get_category(category_id:int,category_service : CategoryService = Depends(get_category_service)):
    return await category_service.get_category_by_id(category_id)

@categoryRouter.patch("/update/{category_id}",status_code=status.HTTP_202_ACCEPTED)
async def update_category(category_id :int, category_name : str = Form(...), image: UploadFile= Form(...),category_service: CategoryService= Depends(get_category_service) ):
    return await category_service.update_category(category_id,category_name,image)