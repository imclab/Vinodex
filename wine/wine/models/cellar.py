from django.db import models
from user import UserProfile
from bottle import Bottle
class Cellar(models.Model):
    owner = models.ForeignKey(UserProfile, related_name="cellars")
    location = models.TextField()
    name = models.TextField()
    photo = models.URLField(null=True, blank=True)
    
    class Meta:
        unique_together = ["owner", "name"]
        app_label = 'wine'

    def num_bottles(self):
        return Bottle.objects.filter(cellar=self).count()
    
    def num_wines(self):
        return len(set([bottle.wine for bottle in Bottle.objects.filter(cellar=self)]))
