import django
from django.utils import unittest
from unittest_helper import UnitTestHelper

class CellarTestCase(django.test.TestCase):


    def setUp(self):
        self.helper = UnitTestHelper(self)

    def test_can_create_and_get_cellar(self):
        user_profile = self.helper.create_profile()
        cellar = {
                "name": "Sample Cellar",
                "location": "Basement",
                "owner": self.helper.remove_hostname(user_profile)
        }
        self.helper.create_and_get_ok("/api/v1/cellar/?format=json", cellar)

    def test_can_delete_cellar(self):
        user_profile = self.helper.create_profile()
        cellar = {
                "name": "Sample Cellar",
                "location": "Basement",
                "owner": self.helper.remove_hostname(user_profile)
        }
        cellar_url = self.helper.postOK("/api/v1/cellar/?format=json", cellar)
        self.helper.deleteOK(cellar_url)

    def test_can_update_cellar(self):
        user_profile = self.helper.create_profile()
        cellar = {
                "name": "Sample Cellar",
                "location": "Basement",
                "owner": self.helper.remove_hostname(user_profile)
        }
        cellar_url = self.helper.postOK("/api/v1/cellar/?format=json", cellar)
        self.helper.putOK(cellar_url, {"name":"Other Cellar"})
        new_cellar = self.helper.getOK(cellar_url)
        self.assertEqual(new_cellar["name"], "Other Cellar")
        self.assertEqual(new_cellar["location"], "Basement")
