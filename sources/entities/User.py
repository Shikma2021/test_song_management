import hashlib
import json
#import Playlist
from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase


class User(object):

    # user_name: str
    # user_password: str
    # friends: []
    # playlists: {}

    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password
        self.friends = []
        self.playlists = {}

    def __repr__(self):
        return json.dumps(dict(
            user_name=self.user_name,
            user_password=self.user_password
        ))

    def parse_password(self, password):
        return hashlib.md5(password.encode()).hexdigest()

    def change_password(self, old_password, new_password):
        if self.parse_password(old_password) == self.password:
            self.password = self.parse_password(new_password)
            return True
        else:
            return None

    def add_friend(self, friend_name):
        if friend_name in self.friends:
            return None
        else:
            self.friends.append(friend_name)
            return friend_name

    def add_playlist(self, playlist_name):
        if playlist_name in self.playlists.keys():
            return None

        self.playlists[playlist_name] = Playlist(playlist_name)
        return playlist_name

    def add_song_to_playlist(self, playlist_name, song_title):
        playlist = self.get_playlist(playlist_name)

        if playlist is None:
            return None

        if song_title not in playlist.get_songs():
            res = playlist.add_song(song_title)
            return res

        return None