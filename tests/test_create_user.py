import allure
import pytest

from data import UserPayloads
from error_messages import FIELD_IS_EMPTY, USER_ALREADY_EXISTS


@allure.feature("Регистрация пользователя")
class TestCreateUser:


    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self, create_new_user):
        user_data, token = create_new_user
        with allure.step("Проверяем, что пользователь создан"):
            assert token is not None
            assert user_data["email"] is not None
            assert user_data["name"] is not None
            assert user_data["password"] is not None


    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_existent_user(self, api_client, create_new_user):
        user_data, _ = create_new_user
        with allure.step("Создаём пользователя"):
            api_client.post("/auth/register", data=user_data)

        with allure.step("Создаём такого же пользователя снова"):
            response = api_client.post("/auth/register", data=user_data)

        with allure.step("Проверяем статус-код 403"):
            assert response.status_code == 403, f"Ожидался 403, получен {response.status_code}"

        with allure.step("Проверяем ответ"):
            expected_response = USER_ALREADY_EXISTS
            assert response.json()["message"] == expected_response, f"Ожидалось '{expected_response}', получено {response.json()}"


    @allure.title("Создание пользователя без одного из обязательных полей")
    @pytest.mark.parametrize("missing_field, payload", UserPayloads.INCOMPLETE_REGISTRATION)
    def test_create_user_with_missing_field(self, api_client, missing_field, payload):
        
        with allure.step(f"Пытаемся создать пользователя без поля '{missing_field}'"):
            response = api_client.post("/auth/register", data=payload)

        with allure.step("Проверяем статус-код 403"):
            assert response.status_code == 403, f"Ожидался 403, получен {response.status_code}"
        
        with allure.step("Проверяем ответ"):
            expected_response = FIELD_IS_EMPTY
            assert response.json()["message"] == expected_response, f"Ожидалось '{expected_response}', получено {response.json()}"