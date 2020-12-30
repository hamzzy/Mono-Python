from pymono import BaseAPI

from pymono import MonoUser


class Mono(BaseAPI, MonoUser):

    def __init__(self):
        super().__init__()

    def Auth(self, code):
        """
        This function Authenticate  the API with key from mono
        :return: user_id
        """

        return self._handle_request("POST", 'account/auth', data=code)

    def getAccount(self) -> dict:
        """
         This function get the User Account after authentication
        :return: json data of a user account
        """
        return self._handle_request("GET", "accounts/" + self.GetUserId())

    def getTransactions(self):
        """
        This function get the User transaction
        :return: json data of a user transactions
        """
        return self._handle_request("GET", f'accounts/{self.GetUserId()}/transactions')

    def getStatement(self, month, type="json"):
        """
        This function get a User Statement of account
        :return: json data of user statement of account
        :return:
        """
        # if type == "json":
        return self._handle_request('GET', f"accounts/{self.GetUserId()}/statement", params=month)
        # if type=="Pdf":
        #     data=self._handle_request('GET', f" accounts/{self.GetUserId()}/statement", param=month)
        #     data[0]['data']

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

    def getUserIdentity(self):
        """
        This function get a User Identity
        :return: json data of user identity
        """
        return self._handle_request("GET", f'accounts/{self.GetUserId()}/identity')

    def bvn_lookup(self, bvn) -> dict:
        """
        This function lookup a user bvn
        :return: json data of a user details
        """
        return self._handle_request("POST", f'v1/lookup/{bvn}/identity')
