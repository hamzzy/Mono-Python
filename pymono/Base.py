import json
import os

import requests
from requests.exceptions import ConnectTimeout, ConnectionError

from pymono.Errors import MissingAuthKeyError


class BaseAPI(object):
    _BASE_URL = "https://api.withmono.com/"

    _CONTENT_TYPE = 'application/json'

    def __init__(self):
        self._MONO_SEC_KEY = os.getenv('MONO-SEC-KEY', None)
        if not self._MONO_SEC_KEY:
            raise MissingAuthKeyError("Missing Authorization key argument or env variable")

    def header(self):
        """
        header function needed
        """
        return {
            'Content-Type': self._CONTENT_TYPE,
            'mono-sec-key': self._MONO_SEC_KEY
        }

    def parse_json(self, response):
        """
        This function takes in every json response sent back by the
        server and trys to get out the important return variables
        Returns a python tuple of status code, status(bool), message, data
        """
        data = response.json()
        return data, response.status_code

    def _url(self, path):
        return self._BASE_URL + path

    def _poll_status(self, data, user_id):
        (data_poll, status_poll) = self._handle_request('GET', f" accounts/{user_id}/statement/jobs/{data.get('id')}")
        return data_poll, status_poll

    def _handle_request(self, method_type, url, data=None, params=None):

        """
        Generic function to handle all API url calls
        Returns a python tuple of status code,data
        """

        payload = json.dumps({"code": data})

        try:
            response = requests.request(url=self._url(url), method=method_type, headers=self.header(),
                                        data=payload, params=params)
            if response.status_code == 400:
                return self.parse_json(response)

            if response.status_code in [200, 201]:
                return self.parse_json(response)
            else:
                return self.parse_json(response)
        except ConnectTimeout:
            return 'The request timed out'
        except ConnectionError:
            return "connection not available"
