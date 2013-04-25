from django.db import models
from django.contrib.gis.db import models

class UserProfile(models.Model):
    email = models.EmailField()
    first_name = models.TextField()
    last_name = models.TextField()
    avatar = models.TextField()

class Winery(models.Model):
    name = models.TextField()
    address = models.TextField()
    location = models.PointField()
    url = models.URLField()

class Cellar(models.Model):
    owner = models.ForeignKey(UserProfile)
    location = models.TextField()
    name = models.TextField()
    photo = models.URLField()

class Wine(models.Model):
    photo = models.TextField()
    winery = models.ForeignKey(Winery)
    vintage = models.TextField()
    wine_type = models.TextField()
    min_price = models.IntegerField()
    max_price = models.IntegerField()
    retail_price = models.IntegerField()
    url = models.URLField()
    label_photo = models.TextField()

class Bottle(models.Model):
    wine = models.ForeignKey(Wine)
    cellar = models.ForeignKey(Cellar)
    photo = models.URLField()
    rating = models.IntegerField()
    price = models.IntegerField()

class Annotation(models.Model):
    bottle = models.ForeignKey(Bottle)
    key = models.TextField()
    value = models.TextField()
