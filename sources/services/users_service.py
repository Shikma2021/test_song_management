import requests
from sources.entities import User
from utils import json_util
import json


def add_user(url, user_name, user_password):
    user = User(user_name, user_password)
    user_json = json.dumps(user.__dict__)
    response = requests.post(url, user_json)


def get_user(url,user_name):
    response = requests.get(url)
    return response



def change_user_password(url, user_name, user_password,new_password):
    fields = [user_name, user_password, new_password]
    user_json = json_util.create_json(fields)
    response = requests.post(url, user_json)


def get_ranked_songs(url,):
    response = requests.get(url)
    return response

def add_friend():



# def remove_friend():
# def remove_all_friends():
#
# def remove_user(url):
#     response = requests.delete(url)
#     return response




