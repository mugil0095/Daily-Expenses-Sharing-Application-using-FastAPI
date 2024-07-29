import pytest
from app.main import app
from httpx import AsyncClient

@pytest.fixture
async def test_client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.mark.asyncio
async def test_create_user(test_client: AsyncClient):
    response = await test_client.post("/users/", json={
        "email": "test@example.com",
        "name": "Test User",
        "mobile_number": "1234567890"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Test User"
