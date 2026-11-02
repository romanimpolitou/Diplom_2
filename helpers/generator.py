
import random
import string


# Генерация случайных данных для нового пользователя
def generate_random_string(length=8):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choices(chars, k=length))

def generate_test_user():
    unique_part = generate_random_string(8)
    name = f"user_{unique_part}"
    email = f"{name}@yandex.ru"
    password = generate_random_string(12)
    return {
        "email": email,
        "password": password,
        "name": name
    }