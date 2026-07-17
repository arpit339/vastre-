from fastapi import FastAPI

from src.routes.user_router import router as user_router
from src.routes.otp_route import router as otp_router

app = FastAPI()

app.include_router(user_router)
app.include_router(otp_router)

