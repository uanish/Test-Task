import pytest
from httpx import AsyncClient
from src.main import app


@pytest.mark.asyncio
async def test_create_question_valid():
    async with AsyncClient(
        app=app, base_url="http://localhost:8000/api/v1/questions/"
    ) as ac:
        response = await ac.post("/", json={"text": ""})
    assert response.status_code == 422
