from django.contrib.gis.db import models
from django.contrib.auth.models import User
class UserProfile(models.Model):
    name = models.TextField()
    avatar = models.URLField(blank=True, null=True)
    user = models.OneToOneField(User, unique=True)

    class Meta:
        app_label='wine'
