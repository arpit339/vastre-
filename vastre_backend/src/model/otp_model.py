from src.db.db_config import Base
from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

class OtpModel(Base):
    __tablename__ = "otp_verifications"

    otp_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(101))
    otp_code: Mapped[str] = mapped_column(String(255))
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    attempts: Mapped[int] = mapped_column(Integer, default=0)
    expires_at: Mapped[DateTime] = mapped_column(DateTime)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    update_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())