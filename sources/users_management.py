import requests
import User
import json


def add_user(url, user_name, user_password):
    user = User(user_name, user_password)
    user_json = json.dumps(user.__dict__)
    response = requests.post(url, user_json)


def get_user(url):
    response = requests.get(url)
    return response


def remove_user(url):
    response = requests.delete(url)
    return response

def change_user_password(url, user_name, user_password,new_password):
    fields = [user_name, user_password, new_password]
    user_json = create_json(fields)
    response = requests.post(url, user_json)


def get_ranked_songs():


def add_friend():


def add_playlist():


def get_playlist():

# def remove_playlist():
# def remove_all_playlists():
# def remove_friend():
# def remove_all_friends():
# def remove_song_from_playlist():
# def remove_all_song_from_playlist():


def create_json(fields):
    for field in fields:
        return str



