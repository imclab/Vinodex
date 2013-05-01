import django
from django.utils import unittest
from unittest_helper import UnitTestHelper

@unittest.skip("Bottle has not yet been implemented")
class BottleTestCase(django.test.TestCase):

    def setUp(self):
        self.helper = UnitTestHelper(self)

    def test_rating_must_be_lte_5(self):
        self.fail("Not implemented")

    def test_rating_must_be_gte_1(self):
        self.fail("Not implemented")

    def test_price_must_be_gt_0(self):
        self.fail("Not implemented")

    def test_can_create_wine(self):
        self.fail("Not implemented")

    def test_can_delete_wine(self):
        self.fail("Not implemented")

    def test_can_update_wine(self):
        self.fail("Not implemented")

    def test_can_get_wine(self):
        self.fail("Not implemented")
