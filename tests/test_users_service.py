import pytest
import configparser
from sources.services.users_service import UserService
from sources.entities import User
from infra.cofig_parser import ConfigParser
from sources.data_helper import *
import pytest_html

configFile = "config.ini"


@pytest.fixture()
def setup_tests():
    # config_parser = ConfigParser.read_configuration(configFile).read()
    # for section in config_parser.sections():
    #     host = config_parser.getint(section,'host')
    #     port = config_parser.getint(section,'port')
    # url = f"http://{host}:{port}"
    url = f"http://127.0.0.1:3002"
    yield url
    # yield
    #delete users & songs


def test_add_user(setup_tests):
    user = create_user()
    url = setup_tests
    UserService.add_user(url, user)
    response = UserService.get_user(url, user.user_name)
    assert user == response


def test_add_existing_user(setup_tests):
    user = create_user()
    url = setup_tests
    UserService.add_user(url, user)
    response = UserService.get_user(url, user.user_name)
    assert user == response


def test_change_user_password():
    user = create_user()
    url = setup_tests
    UserService.add_user(url, user)
    UserService.change_user_password()
    response = UserService.get_user(url, user.user_name)


def test_add_friend(url, user_name):
    UserService .remove_user(url,user_name)


@pytest.mark.xfail("Missing Implementation For Remove User")
def test_remove_user(url, user_name):
    UserService .remove_user(url,user_name)


@pytest.mark.xfail("Missing Implementation For Remove Friend")
def test_remove_friend(url, user_name):
    UserService .remove_user(url,user_name)


@pytest.mark.xfail("Missing Implementation For Removing Friends")
def test_remove_all_friends(url, user_name):
    UserService .remove_user(url,user_name)
