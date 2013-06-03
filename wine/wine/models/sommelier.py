from django.db import models
from abstract import Timestamped
class Sommelier(Timestamped):
    wine_type = models.TextField()
    pairing = models.TextField()
    comment = models.TextField(null=True, blank=True)
    pronounce = models.TextField(null=True, blank=True)
    
    class Meta:
        app_label='wine'
        unique_together = ['wine_type', 'pairing', 'comment', 'pairing']
