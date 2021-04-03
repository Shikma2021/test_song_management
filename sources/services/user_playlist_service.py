from infra.api_manager import api
from sources.services.users_service import UserService
from sources.services.song_sevice import SongService

class UserPlaylistService(UserService):
    PLAYLIST = '/playlists'

    def add_song_to_playlist(self, user, song, playlist):
        url = '{}/{}/add_song'.format(self.baseurl, self.PLAYLIST)
        return api.post(url, dict(
            user_name=user.user_name,
            user_password=user.user_password,
            playlist_name=playlist,
            song_title=song.song_title
        ))

    def add_playlist(self, user, name):
        url = '{}/{}/add_playlist'.format(self.baseurl, self.USERS)
        return api.post(url, dict(
            user_name=user.user_name,
            user_password=user.user_password,
            playlist_name=name
        ))

    def get_playlist(self, user):
        url = '{}/{}/get_playlist'.format(self.baseurl, self.USERS)
        return api.get(url, dict(
            user_name=user.user_name,
            user_password=user.user_password,
            playlist_name=name
        ))