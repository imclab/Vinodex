from django.db import models
from django.contrib.gis.db import models
from abstract import Recognizable, Timestamped

class Winery(Timestamped, Recognizable):
    name = models.TextField(db_index=True)
    address = models.TextField(null=True, blank=True)
    location = models.PointField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    class Meta:
        app_label='wine'
        unique_together = ["name", "address", "location", "url"]
