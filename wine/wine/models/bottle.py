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

    def save(self, *args, **kwargs):
        if self.price is not None and self.price < 0:
            raise ValidationError("Price must be greater than or equal to 0")
        if self.rating is not None and self.rating <= 0:
            raise ValidationError("Rating must be greater than 0")
        if self.rating > 5:
            raise ValidationError("Rating must be less than or equal to 5")

        super(Bottle, self).save(*args, **kwargs)
