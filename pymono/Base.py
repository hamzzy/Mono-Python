import os

import requests
import json

from pymono.Errors import MissingAuthKeyError, InvalidMethodError,Error


class BaseAPI(object):
    _BASE_URL = "https://api.withmono.com/account/"
    _CONTENT_TYPE = 'application/json'

    def __init__(self):
        self._MONO_SEC_KEY = os.getenv('MONO-SEC-KEY', None)
        if not self._MONO_SEC_KEY:
            raise MissingAuthKeyError("Missing Authorization key argument or env variable")

    def _headers(self):
        """
        header function needed
        """
        return {
            'Content-Type': self._CONTENT_TYPE,
            'mono-sec-key': self._MONO_SEC_KEY
        }

    def _parse_json(self, response):
        """
        This function takes in every json response sent back by the
        server and trys to get out the important return variables
        Returns a python tuple of status code, status(bool), message, data
        """
        data = response.json()
        return response.status_code, data

    def _url(self, path):
        return self._BASE_URL + path

    def _handle_request(self, method, url, data=None):

        """
        Generic function to handle all API url calls
        Returns a python tuple of status code,data
        """
        method_type = {
            'GET': requests.get,
            'POST': requests.post,
        }

        payload = json.dumps(data)
        request = method_type.get(method)

        if not request:
            raise InvalidMethodError("Request method not recognised or implemented")

        response = request(self._url(url), headers=self._headers(), data=payload, verify=True)
        if response.status_code == 404:
            raise InvalidMethodError("Not Found")

        if response.status_code in [200, 201]:
            return self._parse_json(response)
        else:
            raise InvalidMethodError("Not connected")


class MonoUser:
    def __init__(self):
        """
        Setter & Getter Class for User Id response
        """
        self.user_id = ""

    def SetUserId(self, user_id):
        """
        This function set a return user id
        """
        self.user_id = user_id

    def GetUserId(self):
        """
         This function get a  user id

         """
        return self.user_id
