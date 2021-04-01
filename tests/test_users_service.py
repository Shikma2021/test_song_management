import pytest
import configparser
from sources.services.users_service import UserService
from sources.entities import User
from infra.cofig_parser import ConfigParser
from sources.create_entities import *

configFile = "config.ini"


@pytest.fixture()
def setup_tests():
    # config_parser = ConfigParser.read_configuration(configFile).read()
    # for section in config_parser.sections():
    #     host = config_parser.getint(section,'host')
    #     port = config_parser.getint(section,'port')
    # url = f"http://{host}:{port}"
    url = f"http://127.0.0.1:3002"
    return url
    # yield
    #teardown


def test_add_user(setup_tests):
    user = create_user()
    url = setup_tests
    UserService.add_user(url, user)
    response = UserService.get_user(url, user.user_name)
    assert user == response


def test_get_user(setup_tests):
    pass
    # UserService.get_user(url, user_name)
    # assert


def test_change_user_password():
    UserService.change_user_password()


@pytest.mark.xfail("Missing Implementation")
def test_remove_user(url, user_name):
    UserService .remove_user(url,user_name)
