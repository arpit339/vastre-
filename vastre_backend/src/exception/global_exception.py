from sqlalchemy.exc import SQLAlchemyError
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.exception.resource_not_found_error import ResourceNotFound


def resource_not_found(request: Request, exc: ResourceNotFound):
    return JSONResponse(status_code=404,
                        content={
                            "error": "Resource not found",
                            "message": exc.message
                        }
                        )

def sqlalchemy_error_handler(request: Request, exc: SQLAlchemyError):
    return JSONResponse(status_code=500,
                        content={
                            "error" : "Database error",
                            "message" : str(exc)
                        })

def unknown_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500,
                        content={
                            "error": "Unknown error",
                            "message" : str(exc)
                        })
