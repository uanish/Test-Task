import pytest
from httpx import AsyncClient
from src.main import app

@pytest.mark.asyncio
async def test_create_user_valid():
    async with AsyncClient(app=app, base_url="http://localhost:8000/api/v1/questions/", follow_redirects=True) as ac:
        response = await ac.post("/", json={"text": ""})
    assert response.status_code == 422

# @pytest.mark.asyncio
# async def test_create_user_empty():
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.post("/users/", json={"name": ""})
#     assert response.status_code == 400
#     assert response.json()["detail"] == "Name cannot be empty"

# @pytest.mark.asyncio
# async def test_create_user_missing():
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.post("/users/", json={})
#     assert response.status_code == 422
