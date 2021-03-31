class Playlist:
    def __init__(self, playlist_name):
        self.name = playlist_name
        self.songs = []

    def add_song(self, song_title,song):
        if song_title in self.get_songs():
            return None

        # song = SongsList.get_song(song_title)

        if song is None:
            return None

        else:
            self.songs.append(song)
            return song_title