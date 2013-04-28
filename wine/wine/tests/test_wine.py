from django.utils import unittest
from unittest_helper import UnitTestHelper
from wine.models import Winery

class WineTestCase(unittest.TestCase):

    def setUp(self):
        self.helper = UnitTestHelper(self)

    def create_winery(self):
        winery = Winery(name="sample winery")
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
        self.fail("Not implemented")

    @unittest.skip("Wine has not yet been implemented")
    def test_can_get_wine(self):
        self.fail("Not implemented")

    @unittest.skip("Wine has not yet been implemented")
    def test_min_price_must_be_lt_max_price(self):
        self.fail("Not implemented")
    
    @unittest.skip("Wine has not yet been implemented")
    def test_min_price_must_be_lt_retail_price(self):
        self.fail("Not implemented")

    @unittest.skip("Wine has not yet been implemented")
    def test_max_price_must_be_gt_retail_price(self):
        self.fail("Not implemented")

    @unittest.skip("Wine has not yet been implemented")
    def test_prices_must_be_gt_0(self):
        self.fail("Not implemented")

    @unittest.skip("Wine has not yet been implemented")
    def test_vintage_must_be_postitive(self):
        self.fail("Not implemented")

