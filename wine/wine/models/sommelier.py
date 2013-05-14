from django.db import models
class Sommelier(models.Model):
    wine_type = models.TextField()
    pairing = models.TextField()
    comment = models.TextField(null=True, blank=True)
    
    class Meta:
        app_label='wine'
