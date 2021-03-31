class User:

    def __init__(self, name, password):
        self.password = self.parse_password(password)
        self.name = name
        self.friends = []
        self.playlists = {}