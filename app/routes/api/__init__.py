from fastapi import APIRouter

from . import health, notification

router = APIRouter()

router.include_router(health.router)
router.include_router(notification.router)
