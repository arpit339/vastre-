from src.db.db_config import Base
from sqlalchemy import Integer,String,Boolean,DateTime,func
from sqlalchemy.orm import Mapped,mapped_column
class UserModel(Base):
    __tablename__ = "users"
    user_id:Mapped[int] = mapped_column(Integer,primary_key=True)
    user_name :Mapped[str] = mapped_column(String(100))
    email : Mapped[str] = mapped_column(String(100))
    password :Mapped[str] = mapped_column(String(100))
    contact : Mapped[str] = mapped_column(String(100))
    is_actice:Mapped[bool] = mapped_column(Boolean,default=True)
    created_at : Mapped[DateTime] = mapped_column(DateTime,default=func.now())
    update_at : Mapped[DateTime] = mapped_column(DateTime,default=func.now(),onupdate=func.now())