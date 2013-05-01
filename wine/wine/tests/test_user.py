import django
from django.utils import unittest
from unittest_helper import UnitTestHelper

class UserTestCase(django.test.TestCase):

    def setUp(self):
        self.helper = UnitTestHelper(self)

    def setUp(self):
        self.helper = UnitTestHelper(self)

    def test_can_create_user(self):
        self.helper.create_user()

    def test_can_delete_user(self):
        user_url = self.helper.create_user()
        return self.helper.deleteOK(user_url)

    def test_can_update_user(self):
        user_url = self.helper.create_user()
        self.helper.putOK(user_url, {"username" : "bob"})
        user_dict = self.helper.getOK(user_url)
        self.assertEqual(user_dict["username"], "bob")


    def test_can_get_user(self):
        user_url = self.helper.create_user()
        user_id = self.helper.current_user_id
        user_dict = self.helper.getOK(user_url) 
        self.assertEqual(user_dict["username"], "sampleUser" +
                str(user_id))
        self.assertEqual(user_dict["email"], "sample" +
                str(user_id) + "@user.com")
        self.assertEqual(user_dict["password"], "password")
