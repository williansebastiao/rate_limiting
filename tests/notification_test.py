import random

import pytest
import pytest_asyncio
import redis.asyncio as aioredis
from fastapi import status
from fastapi.testclient import TestClient

from app.core import settings
from app.main import app


@pytest_asyncio.fixture
async def client():
    with TestClient(app) as test_client:
        yield test_client


@pytest_asyncio.fixture
async def redis_client():
    redis_url = await aioredis.from_url(str(settings.CACHE_DRIVER))
    yield redis_url
    await redis_url.aclose()


@pytest.mark.asyncio
async def test_rate_limit_exceeded(client, redis_client):
    user_id = random.randint(100, 1000)

    for i in range(1, settings.RATE_LIMIT + 2):
        response = client.post(
            "/api/notification",
            headers={"user-id": str(user_id)},
            json={
                "email": "user@example.com",
                "message": "Hello, World!",
                "notification_type": "EMAIL",
            },
        )

        if i > settings.RATE_LIMIT:
            assert response.status_code == status.HTTP_429_TOO_MANY_REQUESTS
            assert response.json() == {"detail": "Too Many Requests"}

    await redis_client.delete(f"user_id: {user_id}")
