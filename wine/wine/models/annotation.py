from django.db import models
from abstract import Timestamped

class Annotation(Timestamped):
    bottle = models.ForeignKey("wine.Bottle", db_index=True)
    key = models.TextField()
    value = models.TextField()

    class Meta:
        app_label ='wine'
