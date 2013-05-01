import django
from django.utils import unittest
from django.contrib.auth.models import User
from unittest_helper import UnitTestHelper

class UserProfileTestCase(django.test.TestCase):


    def setUp(self):
        self.helper = UnitTestHelper(self)

    def test_can_create_profile(self):
        return self.helper.create_profile()

    def test_can_delete_profile(self):
        return self.helper.deleteOK(self.helper.create_profile())

    def test_can_update_profile(self):
        profile_url = self.helper.create_profile()
        self.helper.putOK(profile_url, {"first_name": "Bob"})
        new_profile = self.helper.getOK(profile_url)
        self.assertEquals(new_profile["first_name"], "Bob")
        self.assertEquals(new_profile["last_name"], "User")
        

    def test_can_get_profile(self):
        profile = self.helper.getOK(self.helper.create_profile())
        self.assertEquals(profile["first_name"], "Sample")
        self.assertEquals(profile["last_name"], "User")
