from django.db import models
from django.db.models import DateTimeField

class Timestamped(models.Model):
    class Meta:
        abstract = True

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
