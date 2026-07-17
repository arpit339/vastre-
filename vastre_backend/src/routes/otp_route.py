from fastapi import APIRouter, Depends
from starlette.requests import Request

from src.dependency.service_dependencies import get_otp_service
from src.schema.otp_schema import OtpRequest

router = APIRouter(prefix="/otp", tags=["otp"])

@router.post("/otp")
async def email_submit(request:OtpRequest , otp_service = Depends(get_otp_service)):
    email = request.email
    return await otp_service.get_user(email)