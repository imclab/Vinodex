from django.db import models
from django.contrib.gis.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class UserProfile(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    avatar = models.URLField(blank=True, null=True)
    user = models.OneToOneField(User)

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
    min_price = models.PositiveIntegerField(null=True, blank=True)
    max_price = models.PositiveIntegerField(null=True, blank=True)
    retail_price = models.PositiveIntegerField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    label_photo = models.URLField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if ( self.min_price is not None and self.max_price is not None
             and self.min_price > self.max_price):
            raise ValidationError("Minimum price %d cannot be greater than\
                    maximum price %d" % (self.min_price, self.max_price) )

        if ( self.min_price is not None and self.retail_price is not None and
             self.min_price > self.retail_price):
            raise ValidationError("Minimum price %d cannot be greater than\
                    retail price %d" % (self.min_price, self.retail_price) )

        if ( self.retail_price is not None and self.max_price is not None and
             self.retail_price > self.max_price):
            raise ValidationError("Retail price %d cannot be greater than\
                    maximum price %d" % (self.retail_price, self.max_price) )

        super(Wine, self).save(*args, **kwargs)

class Bottle(models.Model):
    wine = models.ForeignKey(Wine)
    cellar = models.ForeignKey(Cellar)
    photo = models.URLField(null=True, blank=True)
    rating = models.PositiveIntegerField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)

class Annotation(models.Model):
    bottle = models.ForeignKey(Bottle)
    key = models.TextField()
    value = models.TextField()
