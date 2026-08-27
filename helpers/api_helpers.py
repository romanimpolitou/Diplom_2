import allure
import requests

from settings import BASE_ENDPOINT


@allure.step("POST /auth/register: регистрация пользователя")
def create_user(payload): 
    return requests.post(f"{BASE_ENDPOINT}/auth/register", data=payload)


@allure.step("POST /auth/login: авторизация пользователя")
def login_user(payload): 
    return requests.post(f"{BASE_ENDPOINT}/auth/login", data=payload)


@allure.step("POST /orders: создание заказа (token={token})")
def create_order(payload, token=None): 
    headers = {"Authorization": token} if token else {}
    return requests.post(f"{BASE_ENDPOINT}/orders", json=payload, headers=headers)


@allure.step("GET /ingredients: получение списка ингредиентов")
def get_ingredients(): 
    return requests.get(f"{BASE_ENDPOINT}/ingredients")


@allure.step("Проверка наличия accessToken и refreshToken в ответе")
def assert_tokens(response): 
    data = response.json()
    assert "accessToken" in data, "В ответе отсутствует ключ 'accessToken'"
    assert "refreshToken" in data, "В ответе отсутствует ключ 'refreshToken'"