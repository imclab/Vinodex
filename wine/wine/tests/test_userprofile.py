import django
from django.utils import unittest
from django.contrib.auth.models import User
from unittest_helper import UnitTestHelper

class UserProfileTestCase(django.test.TestCase):


    sample_user = {
            "username": "UPSampleUser",
            "password": "Password",
            "email": "sample@user.com"
    }

    def create_user(self):
        url = self.helper.postOK("/api/v1/auth/user/?format=json",
                self.sample_user)

        return "".join(url.split("/")[1:])


    def create_profile(self, user_url):
        profile = {
            "firstname": "Sample",
            "lastname": "User",
            "user": user_url
        }
        return self.helper.postOK("/api/v1/profile/?format=json", profile)


    def setUp(self):
        self.helper = UnitTestHelper(self)

    def test_can_create_profile(self):
        user_url = self.create_user()
        return self.create_profile(self.sample_user)

    @unittest.skip("Not implemented")
    def test_can_delete_profile(self):
        self.fail("Not implemented")

    @unittest.skip("Not implemented")
    def test_can_update_profile(self):
        self.fail("Not implemented")

    @unittest.skip("Not implemented")
    def test_can_get_profile(self):
        self.fail("Not implemented")
