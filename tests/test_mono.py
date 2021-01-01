from . import Mono, TestCase, main, test_mono_key


def assertUUid(uuid):
    if uuid.isalnum():
        return True
    else:
        False


class TestMono(TestCase):

    def setUp(self) -> None:
        super(TestMono, self).setUp()
        self.mono = Mono(code=" ")
        (data, status) = self.mono.Auth()
        self.mono.SetUserId(data.get('id'))

    def test_mono_key(self):
        self.assertNotEqual(test_mono_key, "Missing Authorization key argument or env variable")

    def test_mono_auth(self):
        assertUUid(self.mono.GetUserId())

    def test_mono_Get_Account(self):
        (data, status) = self.mono.getAccount()
        self.assertEqual(status, 200)

    def test_mono_Transaction(self):
        (data, status) = self.mono.getTransactions()
        self.assertEqual(status, 200)

    def test_mono_Transaction_with_filter(self):
        (data, status) = self.mono.getTransactions(start="01-10-2020",end="10-10-2020",types="credit")
        self.assertEqual(status, 200)

    def test_mono_UserCredits(self):
        (data, status) = self.mono.getCredits()
        self.assertEqual(status, 200)

    def test_mono_UserDebits(self):
        (data, status) = self.mono.getDebits()
        self.assertEqual(status, 200)

    def test_mono_UserIdentity(self):
        (data, status) = self.mono.getIdentity()
        self.assertEqual(status, 200)

    def test_mono_getStatement(self):
        (data, status) = self.mono.getStatement("last6month")
        self.assertEqual(status, 200)

    def test_mono_getStatement_pdf(self):
        (data, status) = self.mono.getStatement("last6month", output="pdf")
        self.assertEqual(status, 201)

    # def test_mono_bvn_lookup(self):
    #     (data,status)= self.mono.bvn_lookup("12348994")
    #     self.assertEqual(status, 200)
    #     print(data)


if __name__ == '__main__':
    main()

