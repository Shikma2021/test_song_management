import requests
import json


def validate_res_ok(f):
    def wrapper(*args, **kwargs):
        r = f(*args, **kwargs)

        if r.status_code != 200:
            raise Exception('Error from api: {}'.format(r.text()))

        return r.json()

    return wrapper


class APIManager(object):
    HEADERS = {'Content-Type': 'application/json'}

    def __init__(self):
        pass

    @validate_res_ok
    def get(self, url, **params):
        url = '{}?{}'.format(url, ','.join(['{}={}'.format(k,v) for k,v in params.items()]))

        return requests.get(url, headers=self.HEADERS)

    @validate_res_ok
    def post(self, url, data={}):
        return requests.post(url, json.dumps(data), headers=self.HEADERS)

    @validate_res_ok
    def put(self, url, data={}):
        return requests.put(url, json.dumps(data), headers=self.HEADERS)

    @validate_res_ok
    def delete(self, url):
        return requests.delete(url, headers=self.HEADERS)


api = APIManager()