import unittest

from definition import Account, Advertiser

__unittest = True


class TestAddToDifferentAdvertiser(unittest.TestCase):
    def setUp(self):
        self.alice = Account("alice")
        self.charlie = Advertiser("charlie")
        self.daniel = Advertiser("daniel")
        self.charlie.add_account(self.alice)
        self.daniel.add_account(self.alice)

    def test_owner(self):
        self.assertIsNotNone(self.alice.owner, "Who's my owner?")

    def test_contains(self):
        self.assertNotIn(self.alice, self.charlie, "I shouldn't be in charlie.")
        self.assertIn(self.alice, self.daniel, "I should be one of daniel.")


class TestResetOwner(unittest.TestCase):
    def setUp(self):
        self.alice = Account("alice")
        self.charlie = Advertiser("charlie")
        self.daniel = Advertiser("daniel")
        self.charlie.add_account(self.alice)
        self.alice.set_owner(self.daniel)

    def test_owner(self):
        self.assertIsNotNone(self.alice.owner, "Who's my owner?")

    def test_contains(self):
        self.assertNotIn(self.alice, self.charlie, "I shouldn't be in charlie.")
        self.assertIn(self.alice, self.daniel, "I should be one of daniel.")


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestAddToDifferentAdvertiser("test_owner"))
    suite.addTest(TestAddToDifferentAdvertiser("test_contains"))
    suite.addTest(TestResetOwner("test_owner"))
    suite.addTest(TestResetOwner("test_contains"))
    return suite
