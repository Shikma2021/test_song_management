from sources.services.base_service import BaseService
from sources.entities import User
import json
import requests
from infra.api_manager import api


class UserService:
    USERS = '/users'

    # def add_users(self, users):
    #     if not isinstance(users, list):
    #         users = [users]
    #
    #     uri = '{}/{}/add_user'.format(self.BASE, self.USERS)
    #     for u in users:
    #         yield api.post(uri, u)

    def add_user(url, user):
        url = url + "/users/add_user"
        return requests.post(url, user.__repr__(), headers={'Content-Type':'application/json'})

    def get_user(url, user_name):
        url = f"{url}/users/get_user?user_name={user_name}"
        response = requests.get(url, headers={'Content-Type':'application/json'})
        return response

    def change_user_password(url, user_name, user_password, new_password):
        fields = [user_name, user_password, new_password]
        # user_json = json_util.create_json(fields)
        # response = requests.post(url, user_json)

    def get_ranked_songs(url, operator, rank):
        response = requests.get(url)
        return response

    def add_friend(self):
        pass

    def remove_friend(self):
        pass

    def remove_all_friends(self):
        pass

    def remove_user(self):
        pass
