import django
from django.utils import unittest
from unittest_helper import UnitTestHelper

class SommelierTestCase(django.test.TestCase):


    def setUp(self):
        self.helper = UnitTestHelper(self)

    def test_can_create_and_get_sommelier(self):
        sommelier = {
                "wine_type": "Pinot Noir",
                "pairing": "Cheese"
        }
        self.helper.create_and_get_ok("/api/v1/sommelier/?format=json", sommelier)

    def test_can_delete_sommelier(self):
        sommelier = {
                "wine_type": "Pinot Noir",
                "pairing": "Cheese"
        }
        sommelier_url = self.helper.postOK("/api/v1/sommelier/?format=json", sommelier)
        self.helper.deleteOK(sommelier_url)

    def test_can_update_sommelier(self):
        sommelier = {
                "wine_type": "Pinot Noir",
                "pairing": "Cheese"
        }
        sommelier_url = self.helper.postOK("/api/v1/sommelier/?format=json", sommelier)
        self.helper.putOK(sommelier_url, {"wine_type":"Chardonnay"})
        new_sommelier = self.helper.getOK(sommelier_url)
        self.assertEqual(new_sommelier["wine_type"], "Chardonnay")
        self.assertEqual(new_sommelier["pairing"], "Cheese")
