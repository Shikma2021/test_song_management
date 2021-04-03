import pytest
from sources.services.users_service import UserService
from sources.services.admin_service import AdminService
from infra.cofig_parser import ConfigParser
from sources.data_helper import *
import pytest_html


@pytest.fixture(autouse=True)
def user_service():
    [user_service, admin_service] = ConfigParser.parse([UserService, AdminService])
    yield user_service

    admin_service.delete_all_users()
    admin_service.delete_all_songs()


def test_add_user(user_service):
    '''
    test if users can be added to the system
    :param user_service:
    :return:
    '''
    user = create_user()
    #UserService.add_user(url, user)
    for response in user_service.add_users(user):
        assert response['messgae'] == 'OK'

    validate_user = user_service.get_user(user.user_name)
    assert validate_user['user_name'] == user.user_name


def test_add_friend_to_user(user_service):
    user = create_user()
    friend = create_user()

    for response in user_service.add_users([user, friend]):
        assert response['messgae'] == 'OK'

    assert user_service.add_friend(user, friend)['message'] == 'OK'

    user = user_service.get_user(user.user_name)
    assert friend.user_name in user.friends

def test_fail_add_friend(user_service):
    user = create_user()
    friend = create_user()

    for response in user_service.add_users([user]):
        assert response['messgae'] == 'OK'

    res = user_service.add_friend(user, friend)

    assert 'error' in res

def test_friend_of_friend(user_service):
    user = create_user()
    friend = create_user()

    for response in user_service.add_users([user, friend]):
        assert response['messgae'] == 'OK'

    assert user_service.add_friend(user, friend)['message'] == 'OK'

    friend = user_service.get_user(friend.user_name)
    assert user.user_name in friend.friends

def test_add_friend_twice(user_service):
    user = create_user()
    friend = create_user()

    for response in user_service.add_users([user, friend]):
        assert response['messgae'] == 'OK'

    assert user_service.add_friend(user, friend)['message'] == 'OK'
    assert 'error' in user_service.add_friend(user, friend)

def test_change_password(user_service):
    user = create_user()
    friend = create_user()

    for response in user_service.add_users(user):
        assert response['messgae'] == 'OK'

    new_pass = randomise(5)
    user_service.change_password(user, new_pass)

    res = user_service.add_friend(Bunch(
        user_name=user.user_name,
        user_password=new_pass
    ), friend)
    assert res['message'] == 'OK'


@pytest.mark.xfail("Missing Implementation For Remove User")
def test_remove_user(url, user_name):
    UserService .remove_user(url,user_name)


@pytest.mark.xfail("Missing Implementation For Remove Friend")
def test_remove_friend(url, user_name):
    UserService .remove_user(url,user_name)


@pytest.mark.xfail("Missing Implementation For Removing Friends")
def test_remove_all_friends(url, user_name):
    UserService .remove_user(url,user_name)
