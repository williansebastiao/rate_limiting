from typing import Annotated

import redis.asyncio as aioredis
from fastapi import Header, HTTPException, status

from app.core import settings

redis = aioredis.from_url(str(settings.CACHE_DRIVER))


async def rate_limit_middleware(user_id: Annotated[int, Header()]):
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="X-User-ID header is required",
        )

    key = f"user_id: {user_id}"

    rate_limit = await redis.incr(key)
    if rate_limit == 1:
        await redis.expire(key, settings.CACHE_TIME)

    if rate_limit > settings.RATE_LIMIT:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too Many Requests",
        )

    return True
