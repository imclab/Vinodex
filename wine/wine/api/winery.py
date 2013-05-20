from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from tastypie import fields
from ..models.winery import Winery
from django.contrib.gis.geos import Point

class WineryResource(ModelResource):
    wines = fields.ToManyField("wine.api.WineResource", "wines", null=True)
    class Meta:
        always_return_data = True
        queryset = Winery.objects.all()
        authorization = Authorization()
        excludes = ['location']

    def dehydrate(self, bundle):
        if bundle.obj.location:
            bundle.data["location"] = {
                "lat": bundle.obj.location[0],
                "lon": bundle.obj.location[1]
            }
        return bundle
    
    def hydrate(self, bundle):
        if "location" in bundle.data:
            lat, lon = (bundle.data["location"]["lat"],
                        bundle.data["location"]["lon"])
            bundle.obj.location = Point(lat,lon)
        return bundle
