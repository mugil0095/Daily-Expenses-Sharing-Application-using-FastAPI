import pytest
from app.main import app
from httpx import AsyncClient

@pytest.fixture
async def test_client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.mark.asyncio
async def test_create_expense(test_client: AsyncClient):
    response = await test_client.post("/expenses/expenses/", json={
        "description": "Dinner",
        "amount": 50.0,
        "payer_id": 1,
        "splits": [{"expense_id": 1, "user_id": 2, "amount": 25.0, "percentage": 50.0, "split_type": "equal"}]
    })
    assert response.status_code == 200
    assert response.json()["description"] == "Dinner"
