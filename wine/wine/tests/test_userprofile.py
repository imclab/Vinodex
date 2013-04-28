from django.utils import unittest
from unittest_helper import UnitTestHelper

@unittest.skip("UserProfile has not yet been implemented")
class UserProfileTestCase(unittest.TestCase):
    def setUp(self):
        self.helper = UnitTestHelper(self)

    def test_can_create_profile(self):
        self.fail("Not implemented")

    def test_can_delete_profile(self):
        self.fail("Not implemented")

    def test_can_update_profile(self):
        self.fail("Not implemented")

    def test_can_get_profile(self):
        self.fail("Not implemented")
