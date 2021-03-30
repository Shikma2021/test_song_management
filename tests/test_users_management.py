import pytest
from sources.users_management import add_user

# @pytest.fixture()
# def setup_tests():
#     read_configuration
#     host =
#     port =
#     url = 'http://' + host + ':' + port

@pytest.mark.parametrize("url,user_name,user_password", ["http://localhot:3002/users/add_user","Shikma","AAA"])
def test_add_user(url, user_name, user_password):
    print(add_user(url, user_name, user_password))
