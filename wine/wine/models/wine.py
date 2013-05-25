from django.db import models
from django.contrib.gis.db import models
from winery import Winery
from abstract import Recognizable, Timestamped
from django.core.exceptions import ValidationError
from jsonfield import JSONField

class Wine(Recognizable, Timestamped):
    name = models.TextField(db_index=True)
    photo = models.URLField(null=True, blank=True)
    winery = models.ForeignKey(Winery, related_name="wines", null=True,
            blank=True, db_index=True)
    vintage = models.TextField(null=True, blank=True, db_index=True)
    alcohol_content = models.FloatField(null=True, blank=True, db_index=True)
    wine_type = models.TextField(null=True, blank=True)
    min_price = models.PositiveIntegerField(null=True, blank=True)
    max_price = models.PositiveIntegerField(null=True, blank=True)
    retail_price = models.PositiveIntegerField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    label_photo = models.URLField(null=True, blank=True)
    color = models.TextField(null=True, blank=True)
    raw_data = JSONField(null=True, blank=True)

    class Meta:
        app_label='wine'
        unique_together = \
            ["name",
             "photo",
             "winery",
             "vintage",
             "alcohol_content",
             "wine_type",
             "min_price",
             "max_price",
             "retail_price",
             "url",
             "label_photo",
             "color"]

    def save(self, *args, **kwargs):
        for price in [self.min_price, self.retail_price, self.max_price]:
            if price is not None and price < 0:
                raise ValidationError("Price must be greater than or equal to 0")

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
