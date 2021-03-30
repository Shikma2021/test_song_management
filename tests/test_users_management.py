import pytest
from sources.users_management import add_user
from sources.users_management import get_user

# @pytest.fixture()
# def setup_tests():
#     read_configuration
#     host =
#     port =
#     url = 'http://' + host + ':' + port

@pytest.mark.parametrize("url,user_name,user_password", ["http://localhot:3002/users/add_user","Shikma","AAA"])
def test_add_user(url, user_name, user_password):
    add_user(url, user_name, user_password)
    assert


@pytest.mark.parametrize("url,user_name", ["http://localhot:3002/users/add_user", "Shikma"])
def test_get_user(url, user_password):
    get_user(url, user_name, user_password)
    assert

@pytest.mark.parametrize("url,user_name", ["Shikma"])
def test_remove_user(url, user_password):
    get_user(url, user_name, user_password)
    assert
