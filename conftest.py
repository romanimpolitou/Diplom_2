import pytest

from api_client import APIClient
from helpers.generator import generate_test_user


@pytest.fixture(scope="function")
def api_client():
    return APIClient()

@pytest.fixture
def create_new_user(api_client):
    user_data = generate_test_user()
    response = api_client.post("/auth/register", data=user_data)
    token = response.json().get("accessToken")
    return user_data, token