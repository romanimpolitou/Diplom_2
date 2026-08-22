class UserPayloads:
    INVALID_EMAIL = "non_existent_email"
    INVALID_PASSWORD = "wrong_password"

    INCOMPLETE_REGISTRATION = [
        ("email", {"password": "pass123", "name": "ivan"}),
        ("password", {"email": "ivan@yandex.ru", "name": "ivan"}),
        ("name", {"email": "ivan@yandex.ru", "password": "pass123"}),
    ]