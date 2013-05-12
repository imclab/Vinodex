import django
from django.utils import unittest
from unittest_helper import UnitTestHelper
from wine.models import Winery

class BottleTestCase(django.test.TestCase):

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
        return self.helper.remove_hostname(
                self.helper.postOK("/api/v1/wine/?format=json", sample_wine)
        )

    def create_cellar(self):
        user_profile = self.helper.create_profile()
        cellar = {
                "name": "Sample Cellar",
                "location": "Basement",
                "owner": self.helper.remove_hostname(user_profile)
        }
        return self.helper.remove_hostname(
                self.helper.postOK("/api/v1/cellar/?format=json", cellar)
        )

    def setUp(self):
        self.helper = UnitTestHelper(self)
        self.cellar_url = self.create_cellar()
        self.wine_url = self.create_wine()

    def test_rating_must_be_lte_5(self):
        bottle = {
            "wine": self.wine_url,
            "cellar": self.cellar_url,
            "rating": 6
        }
        self.helper.postBad("/api/v1/bottle/?format=json", bottle)

    def test_rating_must_be_gte_1(self):
        bottle = {
            "wine": self.wine_url,
            "cellar": self.cellar_url,
            "rating": 0 
        }
        self.helper.postBad("/api/v1/bottle/?format=json", bottle)

    def test_price_must_be_gt_0(self):
        bottle = {
            "wine": self.wine_url,
            "cellar": self.cellar_url,
            "price": -5 
        }
        self.helper.postBad("/api/v1/bottle/?format=json", bottle)

    def test_can_create_and_get_bottle(self):
        bottle = {
            "wine": self.wine_url,
            "cellar": self.cellar_url,
            "rating": 4,
            "price": 2.83,
            "photo": "http://www.caminodesantiago.me/wp-content/uploads/water-bottle.jpg"
        }
        url = self.helper.postOK("/api/v1/bottle/?format=json", bottle)
        bottle2 = self.helper.getOK(url)
        self.helper.fields_match(bottle, bottle2, {"cellar", "rating",
            "photo"})

    def test_can_delete_bottle(self):
        bottle = {
            "wine": self.wine_url,
            "cellar": self.cellar_url,
            "rating": 4,
            "price": 2.83,
            "photo": "http://www.caminodesantiago.me/wp-content/uploads/water-bottle.jpg"
        }
        url = self.helper.postOK("/api/v1/bottle/?format=json", bottle)
        self.helper.deleteOK(url)

    def test_can_update_bottle(self):
        bottle = {
            "wine": self.wine_url,
            "cellar": self.cellar_url,
            "rating": 4,
            "price": 2.83,
            "photo": "http://www.caminodesantiago.me/wp-content/uploads/water-bottle.jpg"
        }
        url = self.helper.postOK("/api/v1/bottle/?format=json", bottle)
        self.helper.putOK(url, {"price": 9.98})
        bottle2 = self.helper.getOK(url)
        self.helper.fields_match(bottle, bottle2, {"cellar", "rating",
            "photo"})
        self.assertEquals(bottle2["price"], 9.98)


