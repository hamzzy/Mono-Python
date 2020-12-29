from src import RequestCall, MonoUser


class Mono(RequestCall, MonoUser):

    def __init__(self):

        super().__init__()
        # self.user_id = ""

    def Auth(self, ):
        """

        :return:
        """
        data, status = self.req_call("POST", '/auth', data=self.payload)
        if isinstance("400", status):
            return data
        else:
            # self.user_id = data['id']
            return data

    def GetAccount(self):
        """

        :return:
        """
        data, status = self.req_call("GET", self.GetUserId())
        if isinstance("400", status):
            return data
        else:
            return data

    def GetTransactions(self):
        """

        :return:
        """
        data, status = self.req_call("GET", f'{self.GetUserId()}/transactions')
        if isinstance("400", status):
            return data
        else:
            return data

    def getStatement(self):
        """

        :return:
        """
        pass

    def getUserCredits(self):
        """

        :return:
        """
        data, status = self.req_call("GET", f'{self.GetUserId()}/credits')
        if isinstance("400", status):
            return data
        else:
            return data

    def getUserDebits(self):
        """

        :return:
        """
        data, status = self.req_call("GET", f"{self.GetUserId()}/debits")
        if isinstance("400", status):
            return data
        else:
            return data

    def GetUserIdentity(self):
        """

        :return:
        """
        data, status = self.req_call("GET", f'{self.GetUserId()}/identity')
        if isinstance("400", status):
            return data
        else:
            return data
