# app/tests/conftest.py
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.fixture
async def test_client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
