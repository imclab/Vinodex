from django.db import models
from django.contrib.gis.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.core.cache import cache
from difflib import SequenceMatcher
from scandit import query_scandit_api
from decorators import timed
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
    """
        Exports the names to a given file.
        Important: All of the names must be ascii. Unicode is not allowed, sorry
    """
    handle = open(filename, 'w')
    handle.writelines(names)

class Recognizable(object):
    """
        Mixin for objects that can be recognized from a barcode or wine label.
        In our case, this will be wines and wineries
    """

    # TODO: The cacheing works, but the code is kind of sloppy.
    # Any method that uses the cache should also ensure that the cache is
    # updated. Currently, the cache update status is checked in the public
    # facing methods, which works, but is not good practice.

    def _guess_from_product_name(self, name):
        """
            Returns a list of objects that have a name that's pretty 
            close to the provided name. If no objects could be found,
            this creates a new object with that name, and returns a 
            list containing just that object.
        """
        guesses = self._guess_from_label_text([name])
        if guesses:
            return guesses
        else:
            # TODO: Probably should be self.__class__.create
            return [Wine.create(name=name)]

    def identify_from_barcode(self, barcode):
        """
            Returns a list of objects in our database that could be matched
            to the given barcode
        """
        self._update_name_cache_if_necessary()
        wine_data = query_scandit_api(barcode)
        if wine_data and wine_data.get("basic"):
            return self._guess_from_product_name(wine_data["basic"]["name"]) 
        else:
            return None

    @timed
    def identify_from_label(self, image_filename):
        """
            Returns a list of objects in our database that could be matched
            to the given barcode
        """
        self._update_name_cache_if_necessary()

        # The resulting file has the same name as the filename, but with a ".txt"
        # extension
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
        # TODO: This should be a decorator
        if not cache.get(self._names_cache_key()):
            return self._update_name_cache()

    def _update_name_cache(self):
        all_names = list(set([obj[0].lower().encode('ascii','ignore') for obj in
            self.__class__.objects.values_list('name')]))
        create_data_file(all_names, self._names_filename())
        cache.set(self._names_cache_key(), all_names, 7600)
        return all_names

    def _guess_from_label_text(self, label_lines):
        """
            Looks through all of the lines, and compares each line
            to the list of names. Returns the objects with the name 
            that is the closest match to any line in `label_lines`
        """
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

    def save(self, *args, **kwargs):
        if self.rating <= 0:
            raise ValidationError("Rating must be greater than 0")
        if self.rating > 5:
            raise ValidationError("Rating must be less than or equal to 5")

        super(Bottle, self).save(*args, **kwargs)

class Annotation(models.Model):
    bottle = models.ForeignKey(Bottle, db_index=True)
    key = models.TextField()
    value = models.TextField()

    class Meta:
        unique_together = ["bottle", "key", "value"]

class Sommelier(models.Model):
    wine_type = models.TextField()
    pairing = models.TextField()
