from django.contrib.gis.db import models
from django.contrib.auth.models import User
from abstract import Timestamped
class UserProfile(Timestamped):
    name = models.TextField()
    avatar = models.URLField(blank=True, null=True)
    user = models.OneToOneField(User, unique=True)

    class Meta:
        app_label='wine'
