from django.utils import unittest
from unittest_helper import UnitTestHelper
from wine.models import Winery

class WineTestCase(unittest.TestCase):

    def setUp(self):
        self.helper = UnitTestHelper(self)

    def create_winery(self):
        winery = Winery(name="Sample Winery")
        winery.save()
        return "/api/v1/winery/%d/" % winery.id

    def create_wine(self):
        winery = self.create_winery()
        sample_wine = {
            "name": "Sample Wine",
            "winery": winery
        }
        return self.helper.postOK("/api/v1/wine/?format=json", sample_wine)


    def test_can_create_wine(self):
        return self.create_wine()

    def test_can_delete_wine(self):
        wine = self.create_wine()
        return self.helper.deleteOK(wine)

    def test_can_update_wine(self):
        wine_url = self.create_wine()
        self.helper.putOK(wine_url, {"retail_price": 4.01})
        wine = self.helper.getOK(wine_url)
        self.assertEqual(wine["retail_price"], 4.01)

    def test_can_get_wine(self):
        wine_url = self.create_wine()
        return self.helper.getOK(wine_url)

    def test_min_price_must_be_lte_max_price(self):
        bad_wine = {
            "name": "Sample Wine",
            "winery": self.create_winery(),
            "min_price": 2.00,
            "max_price": 1.00
        }
        return self.helper.postBad("/api/v1/wine/?format=json", bad_wine)
    
    def test_min_price_must_be_lte_retail_price(self):
        bad_wine = {
            "name": "Sample Wine",
            "winery": self.create_winery(),
            "min_price": 2.00,
            "retail_price": 1.00
        }
        return self.helper.postBad("/api/v1/wine/?format=json", bad_wine)

    def test_max_price_must_be_gte_retail_price(self):
        bad_wine = {
            "name": "Sample Wine",
            "winery": self.create_winery(),
            "max_price": 2.00,
            "retail_price": 3.00
        }
        return self.helper.postBad("/api/v1/wine/?format=json", bad_wine)
