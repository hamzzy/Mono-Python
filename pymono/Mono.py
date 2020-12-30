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

        return self._handle_request("POST", 'account/"auth', data=self.code)

    def GetAccount(self) -> dict:
        """
         This function get the User Account after authentication
        :return: json data of a user account
        """
        return self._handle_request("GET", "accounts/" +self.GetUserId())

    def GetTransactions(self):
        """
        This function get the User transaction
        :return: json data of a user transactions
        """
        return self._handle_request("GET", f'accounts/{self.GetUserId()}/transactions')

    def getStatement(self,month):
        """
        This function get a User Statement of account
        :return: json data of user statement of account
        :return:
        """
        return self._handle_request('GET',f" accounts/{self.GetUserId()}/statement?period={month}")

    def getUserCredits(self):
        """
        This function get a User Credits history
        :return: json data of a user credits
        """
        return self._handle_request("GET", f"accounts/{self.GetUserId()}/credits")

    def getUserDebits(self):
        """

        This function get  a User Debits history
        :return: json data of a user debits history
        """
        return self._handle_request("GET", f"accounts/{self.GetUserId()}/debits")

    def GetUserIdentity(self):
        """
        This function get a User Identity
        :return: json data of user identity
        """
        return self._handle_request("GET", f'accounts/{self.GetUserId()}/identity')

    def Bvn_lookup(self,bvn)->dict:
        """
        This function lookup a user bvn
        :return: json data of a user details
        """
        return self._handle_request("POST", f'v1/lookup/{bvn}/identity')
