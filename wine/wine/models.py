from django.db import models
from django.contrib.gis.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.core.cache import cache
from difflib import SequenceMatcher
from tools import query_scandit_api
import subprocess
import tempfile

class UserProfile(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    avatar = models.URLField(blank=True, null=True)
    user = models.OneToOneField(User, unique=True)


class Cellar(models.Model):
    owner = models.ForeignKey(UserProfile, related_name="cellars")
    location = models.TextField()
    name = models.TextField()
    photo = models.URLField(null=True, blank=True)

    class Meta:
        unique_together = ["owner", "name"]

def create_data_file(names, filename):
    handle = open(filename, 'w')
    handle.writelines(names)

class Recognizable(object):

    def _guess_from_product_name(self, name):
        guesses = self._guess_from_label_text([name])
        if guesses:
            return guesses
        else:
            return [Wine.create(name=name)]

    def identify_from_barcode(self, barcode):
        self._update_name_cache_if_necessary()
        wine_data = query_scandit_api(barcode)
        if wine_data and wine_data.get("basic"):
            return self._guess_from_product_name(wine_data["basic"]["name"]) 
        else:
            return None

    def identify_from_label(self, image_filename):
        self._update_name_cache_if_necessary()
        subprocess.call(["tesseract", image_filename, image_filename])
        lines = [line.lower() for line in open(image_filename +
            ".txt").readlines()]
        return self._guess_from_label_text(lines)

    def _names_cache_key(self):
        return self.__class__.__name__ + "_names"

    def _names_filename(self):
        return self.__class__.__name__ + ".dat"

    def _get_names(self):
        return cache.get(self._names_cache_key())

    def _update_name_cache_if_necessary(self):
        if not cache.get(self._names_cache_key()):
            return self._update_name_cache()

    def _update_name_cache(self):
        all_names = list(set([obj[0].lower().encode('ascii','ignore') for obj in
            self.__class__.objects.values_list('name')]))
        create_data_file(all_names, self._names_filename())
        cache.set(self._names_cache_key(), all_names, 7600)
        return all_names

    def _guess_from_label_text(self, label_lines):
        names = self._get_names()
        best_ratio = 0
        best_name = None

        for line in label_lines:
            matcher = SequenceMatcher()
            matcher.set_seq2(line)
            for name in names:
                matcher.set_seq1(name)
                ratio = matcher.ratio()
                if ratio > best_ratio:
                    best_ratio = ratio
                    best_name = name

        if best_name is not None:
            # Filtering by id brings more popular elements to the top
            return self.__class__.objects.filter(name__iexact=best_name).order_by('id')
        else:
            return None
        
class Winery(models.Model, Recognizable):
    name = models.TextField(db_index=True)
    address = models.TextField(null=True, blank=True)
    location = models.PointField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    class Meta:
        unique_together = ["name", "address", "location", "url"]

class Wine(models.Model, Recognizable):
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

class Sommelier(models.Model):
    wine_type = models.TextField()
    pairing = models.TextField()
