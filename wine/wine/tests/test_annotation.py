import django
from django.utils import unittest
from unittest_helper import UnitTestHelper
from wine.models import Winery

class AnnotationTestCase(django.test.TestCase):

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

    def create_bottle(self):
        bottle = {
            "wine": self.create_wine(),
            "cellar": self.create_cellar(),
            "rating": 4,
            "price": 2.83,
            "photo": "http://www.caminodesantiago.me/wp-content/uploads/water-bottle.jpg"
        }
        return self.helper.remove_hostname(
            self.helper.postOK("/api/v1/bottle/?format=json", bottle)
        )

    def setUp(self):
        self.helper = UnitTestHelper(self)
        self.helper = UnitTestHelper(self)
        self.bottle_url = self.create_bottle()

    def test_can_create_and_get_annotation(self):
        annotation = {
                "key": "sample_key",
                "value": "sample_value",
                "bottle": self.bottle_url
                }
        self.helper.create_and_get_ok("/api/v1/annotation/?format=json",
                annotation)

    def test_can_delete_annotation(self):
        annotation = {
                "key": "sample_key",
                "value": "sample_value",
                "bottle": self.bottle_url
                }
        url = self.helper.postOK("/api/v1/annotation/?format=json",
                annotation)
        self.helper.deleteOK(url)

    def test_can_update_annotation(self):
        annotation = {
                "key": "sample_key",
                "value": "sample_value",
                "bottle": self.bottle_url
                }
        url = self.helper.postOK("/api/v1/annotation/?format=json",
                annotation)
        self.helper.putOK(url, {"key": "new_key"})
        annotation2 = self.helper.getOK(url)
        self.assertEquals(annotation2["key"], "new_key")
        self.assertEquals(annotation2["value"], "sample_value")


    def test_annotation_key_cannot_be_null(self):
        annotation = {
                "value": "sample_value",
                "bottle": self.bottle_url
                }
        url = self.helper.postOK("/api/v1/annotation/?format=json",
                annotation)
