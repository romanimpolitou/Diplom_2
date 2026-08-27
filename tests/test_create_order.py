import allure

from error_messages import NO_INGREDIENTS
from helpers.api_helpers import create_order


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_auth(self, api_client, create_new_user):
        _, token = create_new_user
        ingredients = {"ingredients": ["61c0c5a71d1f82001bdaaa6d"]}

        with allure.step("Отправляем POST-запрос на создание заказа"):
            response = create_order(ingredients, token)

        assert response.status_code == 200 and response.json().get("success") is True, \
            f"Ожидался статус 200 и success=True, получен: {response.status_code}, {response.json()}"


    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self, api_client):
        ingredients = {"ingredients": ["61c0c5a71d1f82001bdaaa6d"]}
        
        with allure.step("Отправляем POST-запрос на создание заказа"):
            response = create_order(ingredients)
        
        assert response.status_code == 200 and response.json().get("success") is True, \
            f"Ожидался статус 200 и success=True, получен: {response.status_code}, {response.json()}"


    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self, api_client):
        ingredients = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}

        with allure.step("Отправляем POST-запрос на создание заказа"):
            response = create_order(ingredients)

        assert response.status_code == 200 and response.json().get("success") is True, \
            f"Ожидался статус 200 и success=True, получен: {response.status_code}, {response.json()}"


    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, api_client):
        ingredients = {"ingredients": []}
        
        with allure.step("Отправляем POST-запрос на создание заказа"):
            response = create_order(ingredients)
        
        expected_message = NO_INGREDIENTS
        assert response.status_code == 400 and response.json().get("message") == expected_message, \
            f"Ожидался статус 400 и сообщение '{expected_message}', получен: {response.status_code}, {response.json()}"


    @allure.title("Создание заказа с неправильным хешем ингредиента")
    def test_create_order_with_wrong_hash(self, api_client):
        ingredients = {"ingredients": ["wrong_hash"]}
        
        with allure.step("Отправляем POST-запрос на создание заказа"):
            response = create_order(ingredients)
        
        assert response.status_code == 500, \
            f"Ожидался статус 500, получен: {response.status_code}"