from pymono import BaseAPI

from pymono import MonoUser


class Mono(BaseAPI, MonoUser):

    def __init__(self, code):
        self.code = code
        super().__init__()

    def Auth(self):
        """
        This function Authenticate  the API with key from mono
        :return: tuples user_id,status
        """

        return self._handle_request("POST", 'account/auth', data=self.code)

    def getAccount(self):
        """
         This function get the User Account after authentication
        :return: json data and status
        """
        return self._handle_request("GET", "accounts/" + self.GetUserId())

    def getTransactions(self, start=None, end=None, narration=None, types=None, paginate=None):
        """
        This function get the User transaction
        :return: json data and status
         argument
        :params:start => 01-10-2020
        :params: end => 07-10-2020
        :params:narration => uber
        :params:type => debit or credit
        :params:paginate => bool true or false


        """
        params = {"start": start, "end":end, "narration": narration, "type": types, "paginate": paginate}
        return self._handle_request("GET", f'accounts/{self.GetUserId()}/transactions', params=params)

    def getStatement(self, month, output="json"):
        """
        This function get a User Statement of account
        :return: json data and status
        argument
        :params: month => last6month, last12month
        :params: output => json or pdf
        """

        params = {"period": month, "output": output}
        if output == "Pdf":
            (data, status) = self._handle_request('GET', f"accounts/{self.GetUserId()}/statement", params=params)
            return self._poll_status(data, self.GetUserId())
        else:
            return self._handle_request('GET', f"accounts/{self.GetUserId()}/statement", params=params)

    def getCredits(self):
        """
        This function get a User Credits history
        :return: json data of a user credits
        """

        return self._handle_request("GET", f"accounts/{self.GetUserId()}/credits")

    def getDebits(self):
        """
        This function get  a User Debits history
        :return: json data of a user debits history
        """

        return self._handle_request("GET", f"accounts/{self.GetUserId()}/debits")

    def getIdentity(self):
        """
        This function get a User Identity
        :return: json data of user identity
        """

        return self._handle_request("GET", f'accounts/{self.GetUserId()}/identity')

    def bvn_lookup(self, bvn):
        """
        This function lookup a user bvn
        :return: json data of a user details

        :params bvn -> 123244
        """

        return self._handle_request("POST", f'v1/lookup/{bvn}/identity')
