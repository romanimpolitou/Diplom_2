import allure
import pytest

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

        with allure.step("Проверяем код-статус 200"):
            assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"
            assert response.json()["success"] is True


    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self, api_client):
        ingredients = {"ingredients": ["61c0c5a71d1f82001bdaaa6d"]}
        
        with allure.step("Отправляем POST-запрос на создание заказа"):
            response = create_order(ingredients)
        
        with allure.step("Проверяем код-статус 200"):
            assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"
            assert response.json()["success"] is True


    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self, api_client):
        ingredients = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}

        with allure.step("Отправляем POST-запрос на создание заказа"):
            response = create_order(ingredients)

        with allure.step("Проверяем код-статус 200"):
            assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"
            assert response.json()["success"] is True


    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_without_ingredients(self, api_client):
        ingredients = {"ingredients": []}
        
        with allure.step("Отправляем POST-запрос на создание заказа"):
            response = create_order(ingredients)
        
        with allure.step("Проверяем код-статус 400"):
            assert response.status_code == 400, f"Ожидался 400, получен {response.status_code}"

        with allure.step("Проверяем ответ"):
            expected_response = NO_INGREDIENTS
            assert response.json()["message"] == expected_response, f"Ожидалось '{expected_response}', получено {response.json()}"


    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_wrong_hash(self, api_client):
        ingredients = {"ingredients": ["wrong_hash"]}
        
        with allure.step("Отправляем POST-запрос на создание заказа"):
            response = create_order(ingredients)
        
        with allure.step("Проверяем код-статус 500"):
            assert response.status_code == 500, f"Ожидался 500, получен {response.status_code}"