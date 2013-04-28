from django.db import models
from django.contrib.gis.db import models

class UserProfile(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    avatar = models.TextField()

class Winery(models.Model):
    name = models.TextField()
    address = models.TextField(null=True, blank=True)
    location = models.PointField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)

class Cellar(models.Model):
    owner = models.ForeignKey(UserProfile)
    location = models.TextField()
    name = models.TextField()
    photo = models.URLField(null=True, blank=True)

class Wine(models.Model):
    name = models.TextField()
    photo = models.URLField(null=True, blank=True)
    winery = models.ForeignKey(Winery)
    vintage = models.TextField(null=True, blank=True)
    wine_type = models.TextField(null=True, blank=True)
    min_price = models.IntegerField(null=True, blank=True)
    max_price = models.IntegerField(null=True, blank=True)
    retail_price = models.IntegerField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    label_photo = models.URLField(null=True, blank=True)

class Bottle(models.Model):
    wine = models.ForeignKey(Wine)
    cellar = models.ForeignKey(Cellar)
    photo = models.URLField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

class Annotation(models.Model):
    bottle = models.ForeignKey(Bottle)
    key = models.TextField()
    value = models.TextField()
