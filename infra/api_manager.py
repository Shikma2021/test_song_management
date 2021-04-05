import requests
import json


class APIManager(object):
    HEADERS = {'Content-Type': 'application/json'}

    def __init__(self):
        pass

    def _validate_response(self, r):
        if r.status_code != 200:
            raise Exception('Error from api: {}'.format(r.text()))

        return r.json()

    def get(self, url, **params):
        url = '{}?{}'.format(url, '&'.join(['{}={}'.format(k,v) for k,v in params.items()]))

        return self._validate_response(requests.get(url, headers=self.HEADERS))

    def post(self, url, data={}):
        return self._validate_response(requests.post(url, json.dumps(data), headers=self.HEADERS))

    def put(self, url, data={}):
        return self._validate_response(requests.put(url, json.dumps(data), headers=self.HEADERS))

    def delete(self, url):
        return self._validate_response(requests.delete(url, headers=self.HEADERS))


api = APIManager()