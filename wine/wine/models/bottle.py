from django.db import models
from wine import Wine
from django.core.exceptions import ValidationError
from abstract import Timestamped

class Bottle(Timestamped):
    class Meta:
        app_label='wine'

    wine = models.ForeignKey(Wine)
    cellar = models.ForeignKey("wine.Cellar", db_index=True)
    photo = models.URLField(null=True, blank=True)
    rating = models.PositiveIntegerField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    num_bottles = models.PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):
        if self.price is not None and self.price < 0:
            raise ValidationError("Please input a positive dollar amount")
        if self.rating is not None and self.rating <= 0:
            raise ValidationError("Please rate your wine on a scale from 1-5")
        if self.rating > 5:
            raise ValidationError("Please rate your wine on a scale from 1-5")

        super(Bottle, self).save(*args, **kwargs)
