import unittest

__unittest = True


def get_test_classes(account, advertiser):
    class TestAddToDifferentAdvertiser(unittest.TestCase):
        def setUp(self):
            self.alice = account("alice")
            self.charlie = advertiser("charlie")
            self.daniel = advertiser("daniel")
            self.charlie.add_account(self.alice)
            self.daniel.add_account(self.alice)

        def test_owner(self):
            self.assertIsNotNone(self.alice.owner, "Who's my owner?")

        def test_contains(self):
            self.assertNotIn(self.alice, self.charlie, "I shouldn't be in charlie.")
            self.assertIn(self.alice, self.daniel, "I should be one of daniel.")


    class TestResetOwner(unittest.TestCase):
        def setUp(self):
            self.alice = account("alice")
            self.charlie = advertiser("charlie")
            self.daniel = advertiser("daniel")
            self.charlie.add_account(self.alice)
            self.alice.set_owner(self.daniel)

        def test_owner(self):
            self.assertIsNotNone(self.alice.owner, "Who's my owner?")

        def test_contains(self):
            self.assertNotIn(self.alice, self.charlie, "I shouldn't be in charlie.")
            self.assertIn(self.alice, self.daniel, "I should be one of daniel.")

    return (TestAddToDifferentAdvertiser, TestResetOwner)


def suite(account, advertiser):
    TestAddToDifferentAdvertiser, TestResetOwner = get_test_classes(account, advertiser)
    suite = unittest.TestSuite()
    suite.addTest(TestAddToDifferentAdvertiser("test_owner"))
    suite.addTest(TestAddToDifferentAdvertiser("test_contains"))
    suite.addTest(TestResetOwner("test_owner"))
    suite.addTest(TestResetOwner("test_contains"))
    return suite
