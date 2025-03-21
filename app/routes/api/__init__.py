from fastapi import APIRouter, Depends

from app.middlewares import rate_limit_middleware

from . import health, notification

router = APIRouter()

router.include_router(health.router)
router.include_router(
    notification.router, dependencies=[Depends(rate_limit_middleware)]
)
