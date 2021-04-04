import pytest
from sources.data_helper import *
import pytest_html
from sources.services.admin_service import AdminService
from infra.cofig_parser import ConfigParser
import random


@pytest.fixture()
def admin_service():
    return ConfigParser.parse(AdminService)


def test_delete_all_users(admin_service):
    user = create_user()
    for response in admin_service.add_users(user):
        assert response['messgae'] == 'OK'

    admin_service.delete_all_users()

    user = admin_service.get_user(user.user_name, supress=True)
    assert user is None


def test_delete_all_songs(admin_service):
    song = create_song()
    resp = admin_service.add_song(song)
    assert 'message' in resp and resp['message'] == 'OK'

    admin_service.delete_all_songs()

    song = admin_service.get_song(song.title, supress=True)
    assert song is None


@pytest.mark.xfail("Wrong Implementation")
def test_set_songs(admin_service):
    N = 5
    songs = [create_song() for _ in range(N)]

    admin_service.set_songs(songs)

    song = songs[random.randint(0, N - 1)]
    song = admin_service.get_song(song.title)
    assert song is not None


@pytest.mark.xfail("Wrong Implementation")
def test_set_users(admin_service):
    N = 5
    users = {}
    for _ in range(N):
        n = create_user()
        users[n.name] = n

    admin_service.set_users(users)

    user = users[random.randint(0, N - 1)]
    user = admin_service.get_user(user.user_name)
    assert user is not None