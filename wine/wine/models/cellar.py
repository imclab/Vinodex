from django.db import models
from user import UserProfile
from bottle import Bottle
from abstract import Timestamped
class Cellar(Timestamped):
    owner = models.ForeignKey(UserProfile, related_name="cellars")
    location = models.TextField(null=True, blank=True)
    name = models.TextField()
    photo = models.URLField(null=True, blank=True)
    
    class Meta:
        unique_together = ["owner", "name"]
        app_label = 'wine'

    def num_bottles(self):
        return Bottle.objects.filter(cellar=self).count()
    
    def num_wines(self):
        return len(set([bottle.wine for bottle in Bottle.objects.filter(cellar=self)]))
