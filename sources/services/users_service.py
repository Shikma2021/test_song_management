import requests
from sources.entities import User
from utils import json_util
import json


def add_user(url, user_name, user_password):
    url = url + "/users/add_user"
    user = User(user_name, user_password)
    user_json = json.dumps(user.__dict__)
    response = requests.post(url, user_json)


def get_user(url, user_name):
    response = requests.get(url)
    return response


def change_user_password(url, user_name, user_password, new_password):
    fields = [user_name, user_password, new_password]
    user_json = json_util.create_json(fields)
    response = requests.post(url, user_json)


def get_ranked_songs(url, operator, rank):
    response = requests.get(url)
    return response


def add_friend():
    pass


def remove_friend():
    pass


def remove_all_friends():
    pass


def remove_user(url):
    pass
