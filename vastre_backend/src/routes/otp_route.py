from fastapi import APIRouter, Depends
from starlette.requests import Request

from src.schema.otp_schema import UserResponse
from src.schema.otp_schema import OtpVerify
from src.dependency.service_dependencies import get_otp_service
from src.schema.otp_schema import OtpRequest
from src.utils.jwt import generate_token

router = APIRouter(prefix="/otp", tags=["otp"])


@router.post("/")
async def email_submit(request: OtpRequest, otp_service=Depends(get_otp_service)):
    email = request.email
    await otp_service.get_user(email)
    return {"message": "otp sent"}


@router.post("/verify")
async def verify_otp(
    request: OtpVerify,
    otp_service=Depends(get_otp_service)
):
    result = await otp_service.verify_otp(
        email=request.email,
        otp_code=request.otp_code,
        user_name=request.user_name,
        contact=request.contact,
    )

    token = generate_token({"email": request.email})

    return {
        "token": token,
        "user": result
    }
