from infra.api_manager import api


class SongService(object):

    SONGS = '/songs'
    PLAYLIST = '/playlist'

    def __init__(self, baseurl):
        self.baseurl = baseurl

    def add_song(self, song):
        url = '{}/{}/add_song'.format(self.baseurl, self.SONGS)
        return api.post(url, dict(
            song_genre=song['song_genre'],
            song_year=song['song_year'],
            song_performer=song['song_performer'],
            song_title=song['song_title']
        ))

    def get_song(self, name, supress=False):
        url = '{}/{}/get_song'.format(self.baseurl, self.SONGS)
        resp = api.get(url, song_title=name)
        if not supress:
            assert resp['message'] == 'OK'

        return resp['data'] if 'error' not in resp else None

    def _vote(self, user, song, updown):
        url = '{}/{}/{}'.format(self.baseurl, self.SONGS, updown)
        return api.put(url, dict(
            user_name=user.user_name,
            user_password=user.user_password,
            song_title=song['song_title']
        ))

    def upvote(self, user, song):
        return self._vote(user, song, 'upvote')

    def downvote(self, user, song):
        return self._vote(user, song, 'downvote')

    def search(self, rank, op):
        url = '{}/{}/ranked_songs'.format(self.baseurl, self.SONGS)
        return api.get(url, rank=rank, op=op)