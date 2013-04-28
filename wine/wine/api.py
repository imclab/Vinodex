from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from wine.models import Wine, Winery
from django.contrib.gis.geos import Point

class WineryResource(ModelResource):
    class Meta:
        queryset = Winery.objects.all()
        authorization = Authorization() # TODO: Proper auth
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


def hydrate_price(field, bundle):
    if field in bundle.data:
        price = int(bundle.data[field] * 100.0)
        setattr(bundle.obj, field, price)
        bundle.obj.retail_price = 202
    return bundle

def dehydrate_price(field, bundle):
    if getattr(bundle.obj, field):
        price = float(getattr(bundle.obj, field)) / 100.0
        bundle.data[field] = price
    return bundle


class WineResource(ModelResource):
    winery = fields.ForeignKey(WineryResource, "winery", blank=False)
    class Meta:
        queryset = Wine.objects.all()
        authorization = Authorization() # TODO: Proper auth

    def hydrate(self, bundle):
        for field in ["min_price", "max_price", "retail_price"]:
            bundle = hydrate_price(field, bundle)
        print bundle.obj.retail_price
        return bundle

    def dehydrate(self, bundle):
        for field in ["min_price", "max_price", "retail_price"]:
            bundle = dehydrate_price(field, bundle)
        return bundle
