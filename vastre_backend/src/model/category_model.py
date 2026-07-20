from src.db.db_config import Base
from sqlalchemy import Integer,String,Enum as SQLENUM
from sqlalchemy.orm import Mapped,mapped_column
from enum import Enum 
class CategoryName(str,Enum):
    Wedding = "Wedding"
    Garba = "Garba"
    Jwellary = "Jwellary"


class CategoryModel(Base):
    __tablename__ = "categories"
    category_id :Mapped[int] = mapped_column(Integer,primary_key=True)
    category_name : Mapped[CategoryName] = mapped_column(SQLENUM(CategoryName),nullable=False)
    slug: Mapped[str] = mapped_column(String(500))
    category_image_url :Mapped[str] = mapped_column(String(500),default="\public\categoryImages\lenhga_choli.png")
    category_public_id : Mapped[str] = mapped_column(String(255))