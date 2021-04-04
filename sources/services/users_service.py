from infra.api_manager import api


class UserService:
    USERS = '/users'

    def __init__(self, baseurl):
        self.baseurl = baseurl

    def add_users(self, users):
        if not isinstance(users, list):
            users = [users]

        url = '{}/{}/add_user'.format(self.baseurl, self.USERS)
        for u in users:
            yield api.post(url, u.__dict__)

    def get_user(self, name, supress=False):
        url = '{}/{}/get_user'.format(self.baseurl, self.USERS)
        resp = api.get(url, user_name=name)
        if not supress:
            assert resp['message'] == 'OK'

        return resp['data'] if 'error' not in resp else None

    def add_friend(self, user, friend):
        url = '{}/{}/add_friend'.format(self.baseurl, self.USERS)
        return api.put(url, dict(
            user_name=user.user_name,
            user_password=user.user_password,
            friend_name=friend.user_name
        ))

    def remove_friend(self):
        pass

    def remove_all_friends(self):
        pass

    def remove_user(self):
        pass

    def change_password(self, user, new_pass):
        url = '{}/{}/change_password'.format(self.baseurl, self.USERS)
        return api.put(url, dict(
            user_name=user.user_name,
            user_password=user.user_password,
            user_new_password=new_pass
        ))