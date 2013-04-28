from django.utils import unittest
from unittest_helper import UnitTestHelper
from wine.models import Winery
from test_annotation import AnnotationTestCase


class WineryTestCase(unittest.TestCase):
    sample_winery = {
        "name": "Zack's Winery",
        "address": "Home",
        "url": "http://zackg.me",
        "location": {"lat": 1, "lon": 2}
    }

    def setUp(self):
        self.helper = UnitTestHelper(self)

    def create_winery(self):
        return self.helper.postOK("/api/winery/?format=json", self.sample_winery)

    def test_can_create_winery(self):
        self.create_winery()

    def test_can_get_winery(self):
        winery_url = self.create_winery()
        winery = self.helper.getOK(winery_url)
        self.helper.fields_match(winery, self.sample_winery, ["name", "address", "url",
            "location"])

    def test_can_delete_winery(self):
        # Create a winery
        winery_url = self.create_winery()
        # Ensure deletion works
        response = self.helper.deleteOK(winery_url) 

    def test_can_update_winery(self):
        winery_url = self.create_winery()
        self.helper.putOK(winery_url, {"name": "Arden's Winery"})
        winery = self.helper.getOK(winery_url)
        self.assertEqual(winery["name"], "Arden's Winery")
        self.helper.fields_match(winery, self.sample_winery, ["address", "url", "location"])
