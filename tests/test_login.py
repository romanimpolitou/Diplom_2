import allure

from data import UserPayloads
from error_messages import INCORRECT_DATA


@allure.feature("Авторизация пользователя")
class TestLogin:

    @allure.title("Вход под существующим пользователем")
    def test_login(self, api_client, create_new_user):
        user_data, _ = create_new_user

        with allure.step("Отправляем POST-запрос на auth/login"):
            response = api_client.post("/auth/login", data=user_data)

        assert (response.status_code == 200
                and response.json().get("user", {}).get("email") == user_data["email"]
                and response.json().get("user", {}).get("name") == user_data["name"]), \
            f"Не совпадают ожидаемые данные или статус. Получено: {response.status_code}, {response.json()}"


    @allure.title("Вход с неверным логином и паролем")
    def test_login_with_wrong_data(self, api_client):
        invalid_user = {
            "email": UserPayloads.INVALID_EMAIL,
            "password": UserPayloads.INVALID_PASSWORD
        }
        with allure.step("Отправляем POST-запрос на вход с неверными данными"):
            response = api_client.post("/auth/login", data=invalid_user)

        expected_message = INCORRECT_DATA
        assert response.status_code == 401 and response.json().get("message") == expected_message, \
            f"Ожидался статус 401 и сообщение '{expected_message}', получен: {response.status_code}, {response.json()}"