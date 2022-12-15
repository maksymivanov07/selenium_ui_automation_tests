from api_collections.base_api import BaseAPI


class ReqRes(BaseAPI):
    def __init__(self):
        super().__init__()
        self.__url = 'users'
        self.__url_register = 'register'

    def get_user_by_id(self, user_id):
        return self.get(f'{self.__url}/{user_id}')

    def post_create_user(self):
        return self.post(f'{self.__url_register}')

    def delete_user(self, user_id):
        return self.get(f'{self.__url}/{user_id}')
