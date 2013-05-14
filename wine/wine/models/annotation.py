from django.db import models
from bottle import Bottle

class Annotation(models.Model):
    bottle = models.ForeignKey(Bottle, db_index=True)
    key = models.TextField()
    value = models.TextField()

    class Meta:
        app_label ='wine'
        unique_together = ["bottle", "key", "value"]
