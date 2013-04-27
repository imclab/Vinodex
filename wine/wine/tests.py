from django.utils import unittest
from django.test.client import Client
from test_helpers import getOK, postOK, deleteOK, both_contain
c = Client()
class WineryTestCase(unittest.TestCase):
    data = {
        "name": "Zack's Winery",
        "address": "Home",
        "url": "http://zackg.me",
        "location": {"lat": 1, "lon": 2}
    }

    def create_winery(self):
        return postOK("/api/winery/?format=json", self.data, c, self)

    def test_can_create_winery(self):
        self.create_winery()

    def test_can_get_winery(self):
        winery_url = self.create_winery()
        winery = getOK(winery_url, c, self)
        both_contain(winery, self.data, ["name", "address", "url", "location"],
                self)

    def test_can_delete_winery(self):
        # Create a winery
        winery_url = self.create_winery()
        # Ensure deletion works
        response = deleteOK(winery_url, c, self) 
