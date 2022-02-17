from fastapi import APIRouter

from api.v1 import events, health

api_router = APIRouter()
api_router.include_router(events.router, prefix="/v1/events", tags=["Events"])
api_router.include_router(health.router, prefix="/health", tags=["Health check"])
