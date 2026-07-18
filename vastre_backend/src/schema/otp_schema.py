from pydantic import BaseModel, EmailStr


class OtpRequest(BaseModel):
    email: EmailStr

class OtpVerify(BaseModel):
    email: EmailStr
    otp_code: str
    user_name: str | None = None
    contact: str | None = None

class UserResponse(BaseModel):
    id : int
    email : EmailStr
    token: str