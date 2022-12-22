from selenium_tests.configurations.configuratin_api import BASE_URL
import requests


class BaseAPI:
    def __init__(self):
        self.__base_url = BASE_URL
        self._headers = {'Content-Type': 'application/json'}
        self.__request = requests

    def get(self, url, params=None):
        response = self.__request.get(f'{self.__base_url}{url}', params=params)
        return response

    def post(self, url, body=None, headers=None):
        if body is None:
            body = {"email": "eve.holt@reqres.in", "password": "pistol"}
        if headers is None:
            headers = self._headers
        response = self.__request.post(f'{self.__base_url}{url}', json=body, headers=headers)
        return response

    def delete(self, url, params=None):
        response = self.__request.delete(f'{self.__base_url}{url}', params=params)
        return response
