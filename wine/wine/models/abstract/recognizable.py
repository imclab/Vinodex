from wine.scandit import query_scandit_api
from wine.decorators import timed
from django.core.cache import cache
import subprocess
from django.core.cache import cache
from difflib import SequenceMatcher

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
            return [self.__class__.create(name=name)]

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
