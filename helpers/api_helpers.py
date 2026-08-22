import allure
import requests

from settings import BASE_ENDPOINT


# Отправляем POST-запрос на регистрацию пользователя
def create_user(payload): 
    return requests.post(f"{BASE_ENDPOINT}/auth/register", data=payload)


# Отправляем POST-запрос на авторизацию пользователя
def login_user(payload): 
    return requests.post(f"{BASE_ENDPOINT}/auth/login", data=payload)


# Отправляем POST-запрос на создание заказа
def create_order(payload, token=None): 
    headers = {"Authorization": token} if token else {}
    return requests.post(f"{BASE_ENDPOINT}/orders", json=payload, headers=headers)


# Отправляем GET-запрос на получение списка ингредиентов
def get_ingredients(): 
    return requests.get(f"{BASE_ENDPOINT}/ingredients")


# Проверяем наличие токенов
def assert_tokens(response): 
    data = response.json()
    assert "accessToken" in data, "В ответе отсутствует ключ 'accessToken'"
    assert "refreshToken" in data, "В ответе отсутствует ключ 'refreshToken'"