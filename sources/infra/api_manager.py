import requests

def validate_res_ok(f):
    def wrapper(*a, **kw):
        r = f(*a, **kw)

        if r.status_code != 200:
            raise Exception('Error from api: {}'.format(r.text()))

        return r.json()

    return wrapper

class APIManager(object):

    def __init__(self):
        pass

    @validate_res_ok
    def get(self, url, params):
        url = '{}?{}'.format(url, ','.join(['{}={}'.format(k,v) for k,v in params]))

        return requests.get(uri)

    @validate_res_ok
    def post(self, url, data):
        return self._call('POST', url, data)

    @validate_res_ok
    def put(self, url, data):
        return self._call('PUT', url, data)

    @validate_res_ok
    def delete(self, url, data):
        return self._call('DELETE', url, data)


api = APIManager()