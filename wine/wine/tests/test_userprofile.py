import django
from django.utils import unittest
from django.contrib.auth.models import User
from unittest_helper import UnitTestHelper

class UserProfileTestCase(django.test.TestCase):

    # All users need unique username and passwords. This varible 
    # is used to ensure that all users created have unique usernames
    # and passwords
    current_user_id = 0

    def create_user(self):
        self.current_user_id += 1
        sample_user = {
                "username": "sampleUser" +str(self.current_user_id),
                "password": "password",
                "email": "sample" + str(self.current_user_id) + "@user.com"
        }

        url = self.helper.postOK("/api/v1/auth/user/?format=json", sample_user)

        return "/" + "/".join(url.split("/")[3:])


    def create_profile(self):
        user_url = self.create_user()
        profile = {
            "first_name": "Sample",
            "last_name": "User",
            "user": user_url
        }
        return self.helper.postOK("/api/v1/profile/?format=json", profile)


    def setUp(self):
        self.helper = UnitTestHelper(self)

    def test_can_create_profile(self):
        return self.create_profile()

    def test_can_delete_profile(self):
        return self.helper.deleteOK(self.create_profile())

    def test_can_update_profile(self):
        profile_url = self.create_profile()
        self.helper.putOK(profile_url, {"first_name": "Bob"})
        new_profile = self.helper.getOK(profile_url)
        self.assertEquals(new_profile["first_name"], "Bob")
        self.assertEquals(new_profile["last_name"], "User")
        

    def test_can_get_profile(self):
        profile = self.helper.getOK(self.create_profile())
        self.assertEquals(profile["first_name"], "Sample")
        self.assertEquals(profile["last_name"], "User")
