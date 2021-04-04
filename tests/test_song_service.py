import pytest
from sources.data_helper import *
import pytest_html
from sources.services.song_sevice import SongService
from sources.services.users_service import UserService
from sources.services.admin_service import AdminService
from infra.cofig_parser import ConfigParser


@pytest.fixture()
def services():
    [song_service, user_service, admin_service] = ConfigParser.parse([SongService, UserService, AdminService])

    admin_service.delete_all_users()
    admin_service.delete_all_songs()

    yield [song_service, user_service]


def test_add_song(services):
    songs_service, _ = services
    song = create_song()
    resp = songs_service.add_song(song)
    assert 'message' in resp and resp['message'] == 'OK'

    song = songs_service.get_song(song['song_title'])
    assert song is not None


def test_add_song_twice(services):
    songs_service, _ = services
    song = create_song()
    resp = songs_service.add_song(song)
    assert 'message' in resp and resp['message'] == 'OK'
    resp = songs_service.add_song(song)
    assert 'error' in resp


def test_upvote(services):
    songs_service, user_service = services
    user = create_user()
    song = create_song()

    for response in user_service.add_users(user):
        assert response['messgae'] == 'OK'

    resp = songs_service.add_song(song)
    assert 'message' in resp and resp['message'] == 'OK'

    songs_service.upvote(user, song)

    song = songs_service.get_song(song['song_title'])
    assert song['rating'] == 1


def test_upvote_twice(services):
    songs_service, user_service = services
    user = create_user()
    song = create_song()

    for response in user_service.add_users(user):
        assert response['messgae'] == 'OK'

    resp = songs_service.add_song(song)
    assert 'message' in resp and resp['message'] == 'OK'

    songs_service.upvote(user, song)
    res = songs_service.upvote(user, song)

    assert 'message' not in res or res['message'] != 'OK'


def test_user_notexists_upvote(services):
    songs_service, user_service = services
    user = create_user()
    song = create_song()

    resp = songs_service.add_song(song)
    assert 'message' in resp and resp['message'] == 'OK'

    res = songs_service.upvote(user, song)

    assert 'error' in res


def test_upvote_song_notexists(services):
    songs_service, user_service = services
    user = create_user()
    song = create_song()

    for response in user_service.add_users(user):
        assert response['messgae'] == 'OK'

    res = songs_service.upvote(user, song)
    assert 'error' in res


def test_upvote_wrong_password(services):
    songs_service, user_service = services
    user = create_user()
    song = create_song()

    for response in user_service.add_users(user):
        assert response['messgae'] == 'OK'

    resp = songs_service.add_song(song)
    assert 'message' in resp and resp['message'] == 'OK'

    res = songs_service.upvote(User(
        user_name=user.user_name,
        user_password=randomise(5)
    ), song)

    assert 'error' in res


def test_downvote(services):
    songs_service, user_service = services
    user = create_user()
    song = create_song()

    for response in user_service.add_users(user):
        assert response['messgae'] == 'OK'

    resp = songs_service.add_song(song)
    assert 'message' in resp and resp['message'] == 'OK'

    #upvote by 3
    for u in [create_user() for _ in range(3)]:
        for response in user_service.add_users(u):
            assert response['messgae'] == 'OK'

        songs_service.upvote(u, song)

    songs_service.downvote(user, song)

    song = songs_service.get_song(song['song_title'])
    assert song['rating'] == 2


def test_downvote_not_below_zero(services):
    songs_service, user_service = services
    user = create_user()
    song = create_song()

    for response in user_service.add_users(user):
        assert response['messgae'] == 'OK'

    resp = songs_service.add_song(song)
    assert 'message' in resp and resp['message'] == 'OK'

    songs_service.downvote(user, song)

    song = songs_service.get_song(song['song_title'])
    assert song['rating'] == 0


def test_downvote_twice(services):
    songs_service, user_service = services
    user = create_user()
    song = create_song()

    for response in user_service.add_users(user):
        assert response['messgae'] == 'OK'

    resp = songs_service.add_song(song)
    assert 'message' in resp and resp['message'] == 'OK'

    # upvote by 3
    for u in [create_user() for _ in range(3)]:
        for response in user_service.add_users(u):
            assert response['messgae'] == 'OK'

        songs_service.upvote(u, song)

    songs_service.downvote(user, song)
    songs_service.downvote(user, song)

    song = songs_service.get_song(song['song_title'])
    assert song['rating'] == 2


def test_user_notexists_downvote(services):
    songs_service, user_service = services
    user = create_user()
    song = create_song()

    resp = songs_service.add_song(song)
    assert 'message' in resp and resp['message'] == 'OK'

    res = songs_service.downvote(user, song)

    assert 'error' in res


def test_downvote_song_notexists(services):
    songs_service, user_service = services
    user = create_user()
    song = create_song()

    for response in user_service.add_users(user):
        assert response['messgae'] == 'OK'

    res = songs_service.downvote(user, song)
    assert 'error' in res


def test_downvote_wrong_password(services):
    songs_service, user_service = services
    user = create_user()
    song = create_song()

    for response in user_service.add_users(user):
        assert response['messgae'] == 'OK'

    resp = songs_service.add_song(song)
    assert 'message' in resp and resp['message'] == 'OK'

    res = songs_service.downvote(User(
        user_name=user.user_name,
        user_password=randomise(5)
    ), song)

    assert 'error' in res


def _create_song_with_N_votes(N, services):
    songs_service, user_service = services
    song = create_song()

    resp = songs_service.add_song(song)
    assert 'message' in resp and resp['message'] == 'OK'

    for u in [create_user() for _ in range(N)]:
        for response in user_service.add_users(u):
            assert response['messgae'] == 'OK'

        songs_service.upvote(u, song)


@pytest.mark.parametrize("rank,op", [(3, "eq"), (4, 'less'), (4, 'greater')])
def test_search_songs(services, rank, op):
    songs_service, _ = services
    # create song with 3 votes
    _create_song_with_N_votes(3, services)

    res = songs_service.search(rank, op)
    assert 'message' in res and res['message'] == 'OK' and len(res['data']) == 2

    res = songs_service.search(rank, op)
    assert 'message' in res and res['message'] == 'OK' and len(res['data']) == 2

    res = songs_service.search(rank, op)
    assert 'message' in res and res['message'] == 'OK' and len(res['data']) == 1


def test_search_invalid_op(services):
    songs_service, _ = services

    res = songs_service.search(2, 'XXX')
    assert 'error' in res

