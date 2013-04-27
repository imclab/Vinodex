from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from wine.models import Wine, Winery
from django.contrib.gis.geos import Point

class WineResource(ModelResource):
    class Meta:
        queryset = Wine.objects.all()
        authorization = Authorization() # TODO: Proper auth

class WineryResource(ModelResource):
    class Meta:
        queryset = Winery.objects.all()
        authorization = Authorization() # TODO: Proper auth
        excludes = ['location']

    def dehydrate(self, bundle):
        bundle.data["location"] = {
            "lat": bundle.obj.location[0],
            "lon": bundle.obj.location[1]
            }
        return bundle
    
    def hydrate(self, bundle):
        lat, lon = (bundle.data["location"]["lat"],
                    bundle.data["location"]["lon"])
        bundle.obj.location = Point(lat,lon)
        return bundle

