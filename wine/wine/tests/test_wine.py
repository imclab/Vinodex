from django.utils import unittest
from unittest_helper import UnitTestHelper

@unittest.skip("Wine has not yet been implemented")
class WineTestCase(unittest.TestCase):

    def setUp(self):
        self.helper = UnitTestHelper(self)

    def test_can_create_wine(self):
        self.fail("Not implemented")

    def test_can_delete_wine(self):
        self.fail("Not implemented")

    def test_can_update_wine(self):
        self.fail("Not implemented")

    def test_can_get_wine(self):
        self.fail("Not implemented")

    def test_min_price_must_be_lt_max_price(self):
        self.fail("Not implemented")
    
    def test_min_price_must_be_lt_retail_price(self):
        self.fail("Not implemented")

    def test_max_price_must_be_gt_retail_price(self):
        self.fail("Not implemented")

    def test_prices_must_be_gt_0(self):
        self.fail("Not implemented")

    def test_vintage_must_be_postitive(self):
        self.fail("Not implemented")

