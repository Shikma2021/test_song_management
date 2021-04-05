import random
import string
from sources.entities.User import User


def create_user():
    return User(
        user_name=''.join(random.choices(string.ascii_uppercase, k=10)),
        user_password=''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    )


def randomise(N=5):
    return ''.join(random.choices(string.ascii_uppercase, k=N))


def create_song(year=None):
    return {
        'song_genre': ''.join(random.choices(string.ascii_uppercase, k=4)),
        'song_performer': ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)),
        'song_title': ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)),
        'song_year': random.randint(1900, 2021) if not year else year,
        'rating': 0
    }


def create_new_password():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

