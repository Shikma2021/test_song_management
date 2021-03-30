import requests
import sources.User
import json


def add_user(self, url, user_name, user_password):
    user_json = json.dumps(sources.User.__dict__)
    response = requests.post(url, user_json)
    return response
