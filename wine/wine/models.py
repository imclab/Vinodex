from django.db import models
from django.contrib.gis.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.core.cache import cache
from difflib import SequenceMatcher
import subprocess
import tempfile

class UserProfile(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    avatar = models.URLField(blank=True, null=True)
    user = models.OneToOneField(User, unique=True)

class Winery(models.Model):
    name = models.TextField(db_index=True)
    address = models.TextField(null=True, blank=True)
    location = models.PointField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    
    class Meta:
        unique_together = ["name", "address", "location", "url"]

class Cellar(models.Model):
    owner = models.ForeignKey(UserProfile, related_name="cellars")
    location = models.TextField()
    name = models.TextField()
    photo = models.URLField(null=True, blank=True)

    class Meta:
        unique_together = ["owner", "name"]

class Wine(models.Model):
    name = models.TextField(db_index=True)
    photo = models.URLField(null=True, blank=True)
    winery = models.ForeignKey(Winery, related_name="wines", null=True,
            blank=True, db_index=True)
    vintage = models.TextField(null=True, blank=True, db_index=True)
    wine_type = models.TextField(null=True, blank=True)
    min_price = models.PositiveIntegerField(null=True, blank=True)
    max_price = models.PositiveIntegerField(null=True, blank=True)
    retail_price = models.PositiveIntegerField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    label_photo = models.URLField(null=True, blank=True)

    class Meta:
        unique_together = ["name", "winery", "vintage"]

    @staticmethod
    def guess_wine_from_label_text(label_lines):
        wine_names = Wine.get_wine_names()
        best_ratio = 0
        best_name = None

        for line in label_lines:
            matcher = SequenceMatcher()
            matcher.set_seq2(line)
            for wine_name in wine_names:
                matcher.set_seq1(wine_name)
                ratio = matcher.ratio()
                if ratio > best_ratio:
                    best_ratio = ratio
                    best_name = wine_name

        if best_name is not None:
            wines = Wine.objects.filter(name__iexact=best_name)
            if wines:
                return wines[0]
            else:
                # The wine was in the cache, but it must have been deleted since
                # then
                return None
        else:
            return None

    @staticmethod
    def identify_from_label(image_filename):
        subprocess.call(["tesseract", image_filename, image_filename])
        lines = [line.lower() for line in open(image_filename +
            ".txt").readlines()]
        print lines
        return Wine.guess_wine_from_label_text(lines)

    @staticmethod
    def create_name_cache(ttl_seconds):
        all_wine_names = list(set([obj[0].lower().encode('ascii','ignore') for obj in
            Wine.objects.values_list('name')]))
        print all_wine_names[:10]
        Wine.create_data_file(all_wine_names, "wine_names.dat")
        cache.set('wine_names', all_wine_names, ttl_seconds)
        return all_wine_names

    @staticmethod
    def get_wine_names():
        names = cache.get('wine_names')
        if names:
            return names
        else:
            return Wine.create_name_cache(7200)

    @staticmethod
    def create_data_file(wine_names, filename):
        handle = open(filename, 'w')
        handle.writelines(wine_names)

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
    cellar = models.ForeignKey(Cellar, db_index=True)
    photo = models.URLField(null=True, blank=True)
    rating = models.PositiveIntegerField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)

class Annotation(models.Model):
    bottle = models.ForeignKey(Bottle, db_index=True)
    key = models.TextField()
    value = models.TextField()

    class Meta:
        unique_together = ["bottle", "key", "value"]
