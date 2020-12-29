from pymono import BaseAPI, MonoUser
import json


class Mono(BaseAPI, MonoUser):

    def __init__(self, code: str):
        super().__init__()
        self.code = code

    def Auth(self):
        """
        This function Authenticate  the API with key from mono
        :return: user_id
        """

        return self._handle_request("POST", 'auth', data=self.code)

    def GetAccount(self) -> dict:
        """
         This function get the User Account after authentication
        :return: json data of a user account
        """
        return self._handle_request("GET", self.GetUserId())

    def GetTransactions(self):
        """
        This function get the User transaction
        :return: json data of a user transactions
        """
        return self._handle_request("GET", f'{self.GetUserId()}/transactions')

    def getStatement(self):
        """
        This function get a User Statement of account
        :return: json data of user statement of account
        :return:
        """
        pass

    def getUserCredits(self):
        """
        This function get a User Credits history
        :return: json data of a user credits
        """
        return self._handle_request("GET", f'{self.GetUserId()}/credits')

    def getUserDebits(self):
        """

        This function get  a User Debits history
        :return: json data of a user debits history
        """
        return self._handle_request("GET", f"{self.GetUserId()}/debits")

    def GetUserIdentity(self):
        """
        This function get a User Identity
        :return: json data of user identity
        """
        return self._handle_request("GET", f'{self.GetUserId()}/identity')
