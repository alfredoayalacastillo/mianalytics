import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_health_endpoint():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["service"] == "MIANALITICS"
    assert data["status"] == "online"

@pytest.mark.asyncio
async def test_lead_score_endpoint():
    payload = {
        "deal_value": 45000,
        "interactions_count": 12,
        "days_in_pipeline": 8
    }
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/api/v1/predict/lead-score", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "close_probability" in data
    assert "score_category" in data

@pytest.mark.asyncio
async def test_cross_validation_endpoint():
    payload = {
        "dataset_name": "deals",
        "n_splits": 5
    }
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/api/v1/train/cross-validate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["n_splits"] == 5
    assert len(data["scores"]) == 5
