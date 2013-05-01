import django
from django.utils import unittest
from unittest_helper import UnitTestHelper

class AnnotationTestCase(django.test.TestCase):


    def setUp(self):
        self.helper = UnitTestHelper(self)

    def test_can_create_and_get_cellar(self):
        user_profile = self.helper.create_profile()
        cellar = {
                "name": "Sample Cellar",
                "location": "Basement",
                "profile": self.helper.remove_hostname(user_profile)
        }
        helper.create_and_get_ok("/api/v1/cellar/?format=json", cellar)

    def test_can_delete_cellar(self):
        self.fail("Not implemented")

    def test_can_update_cellar(self):
        self.fail("Not implemented")

    def test_can_get_cellar(self):
        self.fail("Not implemented")

