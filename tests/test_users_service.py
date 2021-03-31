import pytest
from sources.services import users_service
from sources.entities import User
from sources.conf_reader import ConfReader

configFile = "config.ini"
scenarioFile = "Scenario-1.ini"

@pytest.fixture()
def setup_tests():
    user = ConfReader.read_configuration()


@pytest.mark.parametrize("url,user_name,user_password", ["http://localhot:3002/users/add_user","Shikma","AAA"])
def test_add_user(url, setup_test):
    users_service.add_user(url, user_name, user_password)
    # assert


def test_get_user(setup_tests):
    users_service.get_user(url, user_name)
    # assert


def test_change_user_password():
    users_service.change_user_password()


@pytest.mark.xfail("Missing Implementation")
def test_remove_user(url, user_name):
    users_service.remove_user(url,user_name)
