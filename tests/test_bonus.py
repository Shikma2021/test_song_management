import pytest
from sources.services.users_service import UserService
from infra.cofig_parser import ConfigParser
from sources.data_helper import *
from infra.file_util import *
import pytest_html


@pytest.fixture(autouse=True)
def settings():
    user_service, config = ConfigParser.parse(UserService, with_config=True)
    yield user_service, config


def test_check_password(settings):
    user_service, config = settings
    user = create_user()

    for _ in user_service.add_users(user):
        pass

    users_json = load_json_file(config['users']['db_path'])
    assert users_json[user.user_name]['password'] != user.user_password