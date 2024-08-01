from fastapi import APIRouter
from .routers import routes

api_router = APIRouter()
api_router.include_router(routes.router, prefix="/v1")

