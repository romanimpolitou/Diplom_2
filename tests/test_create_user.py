import allure
import pytest

from data import UserPayloads
from error_messages import FIELD_IS_EMPTY, USER_ALREADY_EXISTS


@allure.feature("Регистрация пользователя")
class TestCreateUser:


    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self, create_new_user):
        user_data, token = create_new_user
        with allure.step("Получаем данные созданного пользователя и токен из фикстуры"):
            pass

        assert token is not None and user_data["email"] is not None, \
            "Ожидались токен и email, но одно из значений отсутствует"


    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_existent_user(self, api_client, create_new_user):
        user_data, _ = create_new_user

        with allure.step("Создаём пользователя повторно (ожидаем ошибку)"):
            response = api_client.post("/auth/register", data=user_data)

        expected_message = USER_ALREADY_EXISTS
        assert response.status_code == 403 and response.json().get("message") == expected_message, \
            f"Ожидался статус 403 и сообщение '{expected_message}', получен: {response.status_code}, {response.json()}"


    @allure.title("Создание пользователя без одного из обязательных полей")
    @pytest.mark.parametrize("missing_field, payload", UserPayloads.INCOMPLETE_REGISTRATION)
    def test_create_user_with_missing_field(self, api_client, missing_field, payload):
        
        with allure.step(f"Пытаемся создать пользователя без поля '{missing_field}'"):
            response = api_client.post("/auth/register", data=payload)

        expected_message = FIELD_IS_EMPTY
        assert response.status_code == 403 and response.json().get("message") == expected_message, \
            f"Ожидался статус 403 и сообщение '{expected_message}', получен: {response.status_code}, {response.json()}"