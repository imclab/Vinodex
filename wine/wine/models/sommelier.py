from django.db import models
from abstract import Timestamped
class Sommelier(Timestamped):
    wine_type = models.TextField()
    pairing = models.TextField()
    comment = models.TextField(null=True, blank=True)
    
    class Meta:
        app_label='wine'
