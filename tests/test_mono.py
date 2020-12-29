from . import Mono, BaseAPI, TestCase, main, test_mono_key


class TestMono(TestCase):

    def setUp(self) -> None:
        super(TestMono, self).setUp()
        self.mono = Mono.Mono(code='has7tgas7t73')
        # self.user_id = self.mono.GetUserId()

    def test_mono_key(self):
        self.assertNotEqual(test_mono_key, "Missing Authorization key argument or env variable")

    def test_mono_auth(self):
        status, data = self.mono.Auth()
        print(data)
        self.mono.SetUserId(data['id'])

    # def test_mono_Get_Account(self):
    #     status, data = self.mono.GetAccount()
    #     self.assertEqual(status, 200)
    #
    # def test_mono_Transaction(self):
    #     status, data = self.mono.GetAccount()
    #     self.assertEqual(status, 200)


if __name__ == '__main__':
    main()
