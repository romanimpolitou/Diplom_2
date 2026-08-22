import requests

from settings import BASE_ENDPOINT


class APIClient:
    def post(self, endpoint, data=None):
        url = f"{BASE_ENDPOINT}{endpoint}"
        return requests.post(url, json=data)