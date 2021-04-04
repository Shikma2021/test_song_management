import hashlib
import json
#import Playlist
#from dataclasses import dataclass
#from dataclasses_json import dataclass_json, LetterCase


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