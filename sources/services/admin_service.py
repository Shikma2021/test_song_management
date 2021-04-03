from infra.api_manager import api
from sources.services.users_service import UserService
from sources.services.song_sevice import SongService

class AdminService(UserService, SongService):
    ADMIN = '/admin'

    def delete_all_users(self):
        url = '{}/{}/delete_all_users'.format(self.baseurl, self.ADMIN)
        return api.delete(url)

    def delete_all_songs(self):
        url = '{}/{}/delete_all_songs'.format(self.baseurl, self.ADMIN)
        return api.delete(url)

    def set_songs(self, songs):
        url = '{}/{}/set_songs'.format(self.baseurl, self.ADMIN)
        return api.post(url, dict(songs=songs))

    def set_users(self, users):
        url = '{}/{}/set_users'.format(self.baseurl, self.ADMIN)
        return api.post(url, dict(users=users))