from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from wine.models import Wine, Winery
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User
import traceback

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        authorization =Authorization() # TODO: Proper auth

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

def hydrate_once(hydrate_function):
    """ Ensures that the given field hydration function is only
       every applied once to the given object. This is necessary to ensure
       that the prices are properly converted to the correct format when
       being sent between the client and the server """

    def wrapper(*args, **kwargs):
        """ Assumes that the first argument passed is the field, and the 
            second argument passed in is the bundle """
        field, bundle = args

        # If the field has not already been hydrated, set the hydration flag
        # for that field and run the hydration function
        if not hasattr(bundle, field+"_hydrated"):
            setattr(bundle, field + "_hydrated", True)
            return hydrate_function(*args, **kwargs)

        # Otherwise just return the original bundle
        return bundle

    return wrapper

@hydrate_once
def hydrate_price(field, bundle):
    """ When the price is sent to the server, create the integer representation
        that the database will store """
    if field in bundle.data:
        price = int(bundle.data[field] * 100.0)
        bundle.data[field] = price
    return bundle

def dehydrate_price(field, bundle):
    """ When returning the price to the client, return the floating point value
        that represents the correct price"""
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
        """ Convert client-side floating-point price representation into
            the server-side representation """
        for field in ["min_price", "max_price", "retail_price"]:
            bundle = hydrate_price(field, bundle)
        return bundle

    def dehydrate(self, bundle):
        """ Convert server-side integer price representation into
            the client-side floating-point representation """
        for field in ["min_price", "max_price", "retail_price"]:
            bundle = dehydrate_price(field, bundle)
        return bundle
