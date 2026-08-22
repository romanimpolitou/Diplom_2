import allure
import pytest
import requests

from data import UserPayloads
from error_messages import INCORRECT_DATA
from helpers.api_helpers import assert_tokens


@allure.feature("Авторизация пользователя")
class TestLogin:

    @allure.title("Вход под существующим пользователем")
    def test_login(self, api_client, create_new_user):
        user_data, _ = create_new_user

        with allure.step("Отправляем POST-запрос на auth/login"):
            response = api_client.post("/auth/login", data=user_data)

        with allure.step("Проверяем код-статус 200"):
            assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

        with allure.step("Проверяем токены"):
            assert_tokens(response)

        with allure.step("Проверяем соответствие емейла и юзернейма"):
            assert response.json()["user"]["email"] == user_data["email"]
            assert response.json()["user"]["name"] == user_data["name"]


    @allure.title("Вход с неверным логином и паролем")
    def test_login_with_wrong_data(self, api_client):
        invalid_user = {
            "email": UserPayloads.INVALID_EMAIL,
            "password": UserPayloads.INVALID_PASSWORD
        }
        with allure.step("Отправляем POST-запрос на вход с неверными данными"):
            response = api_client.post("/auth/login", data=invalid_user)

        with allure.step("Проверяем код-статус 401"):
            assert response.status_code == 401, f"Ожидался 401, получен {response.status_code}"

        with allure.step("Проверяем ответ"):
            expected_response = INCORRECT_DATA
            assert response.json()["message"] == expected_response, f"Ожидалось '{expected_response}', получено {response.json()}"