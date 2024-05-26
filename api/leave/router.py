from fastapi import APIRouter
from api.leave.controller import leave_router

leave_api_router = APIRouter()
leave_api_router.include_router(leave_router, tags=["leave"])

