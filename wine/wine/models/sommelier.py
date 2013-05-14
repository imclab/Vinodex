from django.db import models
class Sommelier(models.Model):
    wine_type = models.TextField()
    pairing = models.TextField()
    
    class Meta:
        app_label='wine'
