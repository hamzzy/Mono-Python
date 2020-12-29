import os

import requests

BASE_URL = "https://api.withmono.com/account/"


class RequestCall:
    def __init__(self):
        self.header = {
            'Content-Type': 'application/json',
            'mono-sec-key': os.getenv('MONO-SEC-KEY')
        }
        self.payload = {"code": os.getenv('MONO-CODE')}

    def req_call(self, req, url, data=None):
        request = requests.request(req, url=f'{BASE_URL}{url}', headers=self.header, data=data)

        return request.json(), request.status_code


class MonoUser:
    def __init__(self):
        self.user_id = ""

    def SetUserId(self, user_id):
        self.user_id = user_id

    def GetUserId(self):
        return self.user_id
