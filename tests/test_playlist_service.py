import pytest
from sources.data_helper import *
import pytest_html
from sources.services.song_sevice import SongService
from sources.services.user_playlist_service import UserPlaylistService
from sources.services.admin_service import AdminService
from infra.cofig_parser import ConfigParser

@pytest.fixture()
def services():
    [song_service, user_playlist_service, admin_service] = ConfigParser.parse([SongService, UserPlaylistService, AdminService])
    yield [song_service, user_playlist_service]

    admin_service.delete_all_users()
    admin_service.delete_all_songs()


def test_add_song_to_playlist(services):
    songs_service, playlist_service = services
    user = create_user()
    song = create_song()
    playlist = randomise(5)

    for response in playlist_service.add_users(user):
        assert response['messgae'] == 'OK'

    resp = songs_service.add_song(song)
    assert 'message' in resp and resp['message'] == 'OK'

    playlist_service.add_playlist(user, playlist)
    res = playlist_service.add_song_to_playlist(user, song, playlist)

    assert 'message' in res and res['message'] == 'OK'

def test_add_song_twice_to_playlist(services):
    songs_service, playlist_service = services
    user = create_user()
    song = create_song()
    playlist = randomise(5)

    for response in playlist_service.add_users(user):
        assert response['messgae'] == 'OK'

    resp = songs_service.add_song(song)
    assert 'message' in resp and resp['message'] == 'OK'

    playlist_service.add_playlist(user, playlist)
    playlist_service.add_song_to_playlist(user, song, playlist)
    res = playlist_service.add_song_to_playlist(user, song, playlist)

    assert 'error' in res

def test_add_same_playlist_name_to_mul_users(services):
    _, playlist_service = services
    playlist = randomise(5)

    for u in [create_user() for _ in range(3)]:
        for response in playlist_service.add_users(u):
            assert response['messgae'] == 'OK'

        res = playlist_service.add_playlist(u, playlist)
        assert 'message' in res and res['message'] == 'OK'

def test_add_playlist(services):
    _, playlist_service = services
    user = create_user()
    playlist_name = randomise(5)

    for response in playlist_service.add_users(user):
        assert response['messgae'] == 'OK'

    playlist_service.add_playlist(user, playlist_name)

    user = playlist_service.get_user(user.user_name)
    assert playlist_name in user['playlists']

def test_add_playlist_twice(services):
    _, playlist_service = services
    user = create_user()
    playlist_name = randomise(5)

    for response in playlist_service.add_users(user):
        assert response['messgae'] == 'OK'

    playlist_service.add_playlist(user, playlist_name)

    tmp = playlist_service.get_user(user.user_name)
    assert playlist_name in tmp['playlists']

    assert 'error' in playlist_service.add_playlist(user, playlist_name)

def test_add_playlist_to_noexisting_user(services):
    _, playlist_service = services
    user = create_user()
    playlist_name = randomise(5)

    assert 'error' in playlist_service.add_playlist(user, playlist_name)

def test_get_playlist(services):
    _, playlist_service = services
    user = create_user()
    playlists = [randomise(5) for _ in range(4)]

    for response in playlist_service.add_users(user):
        assert response['messgae'] == 'OK'

    for playlist in playlists:
        playlist_service.add_playlist(user, playlist)

    user = playlist_service.get_user(user.user_name)
    assert all([pl in user['playlists'] for pl in playlists])

def test_add_playlist_with_wrong_user(services):
    songs_service, playlist_service = services
    user = create_user()
    song = create_song()
    playlist = randomise(5)

    for response in playlist_service.add_users(user):
        assert response['messgae'] == 'OK'

    resp = songs_service.add_song(song)
    assert 'message' in resp and resp['message'] == 'OK'

    res = playlist_service.add_playlist(dict(
        user_name=user.user_name,
        user_password=randomise(5)
    ), playlist)

    assert 'error' in res

