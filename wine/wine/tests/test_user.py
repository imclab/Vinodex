import django
from django.utils import unittest
from unittest_helper import UnitTestHelper

class UserTestCase(django.test.TestCase):
    sample_user1 = {
        "username": "Sample User",
        "email": "sampleuser@email.com",
        "password": "password"
    }

    sample_user2 = {
        "username": "Sample User2",
        "email": "sampleuser2@email.com",
        "password": "password"
    }

    sample_user3 = {
        "username": "Sample User3",
        "email": "sampleuser3@email.com",
        "password": "password"
    }

    sample_user4 = {
        "username": "Sample User4",
        "email": "sampleuser4@email.com",
        "password": "password"
    }

    def setUp(self):
        self.helper = UnitTestHelper(self)

    def create_user1(self):
        return self.helper.postOK("/api/v1/auth/user/?format=json", self.sample_user1)

    def create_user2(self):
        return self.helper.postOK("/api/v1/auth/user/?format=json", self.sample_user2)

    def create_user3(self):
        return self.helper.postOK("/api/v1/auth/user/?format=json", self.sample_user3)

    def create_user4(self):
        return self.helper.postOK("/api/v1/auth/user/?format=json", self.sample_user4)

    def setUp(self):
        self.helper = UnitTestHelper(self)

    def test_can_create_user(self):
        self.create_user1()

    def test_can_delete_user(self):
        user_url = self.create_user3()
        return self.helper.deleteOK(user_url)

    def test_can_update_user(self):
        user_url = self.create_user4()
        self.helper.putOK(user_url, {"username" : "bob"})
        user_dict = self.helper.getOK(user_url)
        self.assertEqual(user_dict["username"], "bob")


    def test_can_get_user(self):
        user_url = self.create_user2()
        user_dict = self.helper.getOK(user_url) 
        self.helper.fields_match(self.sample_user2, user_dict, ["username","email","password"])
        self.assertEqual(user_dict["password"], "password")
