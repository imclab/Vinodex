from django.db import models
from user import UserProfile
class Cellar(models.Model):
    owner = models.ForeignKey(UserProfile, related_name="cellars")
    location = models.TextField()
    name = models.TextField()
    photo = models.URLField(null=True, blank=True)

    class Meta:
        unique_together = ["owner", "name"]
        app_label = 'wine'
