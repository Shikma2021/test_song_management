import random
import string
from entities.User import User


def create_user():
    return User(
        user_name=''.join(random.choices(string.ascii_uppercase, k=10)),
        user_password=''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    )
