"""Tests for health endpoint."""

from httpx import AsyncClient


async def test_health_check(client: AsyncClient):
    """Test health check endpoint returns expected structure."""
    response = await client.get("/health")

    assert response.status_code == 200
    data = response.json()

    assert "status" in data
    assert "version" in data
    assert "services" in data
    assert data["version"] == "6.0.0"


async def test_root_endpoint(client: AsyncClient):
    """Test root endpoint returns API info."""
    response = await client.get("/")

    assert response.status_code == 200
    data = response.json()

    assert data["name"] == "Token Metering API"
    assert "endpoints" in data
    assert "metering" in data["endpoints"]
    assert "balance" in data["endpoints"]
    assert "admin" in data["endpoints"]
