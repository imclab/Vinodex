from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from tastypie.serializers import Serializer
from tastypie import fields
from wine.models import (Wine, Winery, UserProfile, Cellar, Sommelier, Bottle,
                        Annotation)
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User
import traceback
from django.http import (HttpResponse, HttpResponseBadRequest,
                        HttpResponseNotFound)

class UserResource(ModelResource):
    profile = fields.ToOneField("wine.api.UserProfileResource", "profile",
                                null=True)
    class Meta:
        resource_name = "auth/user"
        queryset = User.objects.all()
        authorization = Authorization() # TODO: Proper auth

class UserProfileResource(ModelResource):
    user = fields.ToOneField(UserResource, "user", blank=False)
    cellars =\
    fields.ToManyField("wine.api.CellarResource","cellars",related_name="owner",
            blank=True)
    class Meta:
        resource_name = "profile"
        queryset = UserProfile.objects.all()
        authorization = Authorization()

    def obj_create(self, bundle, **kwargs):
        if not bundle.data.get("email") and not bundle.data.get("password"):
            return super(UserProfileResource, self).obj_create(bundle, **kwargs)
        else:
            email = bundle.data.get("email")
            password = bundle.data.get("password")
            user = User.objects.create(email=email,username=email,password=password)
            bundle.obj = UserProfile.objects.create(name=bundle.data.get("name"),
                                                    user=user)
            bundle.obj.user = user
            bundle.obj.save()
            return bundle

class CellarResource(ModelResource):
    owner = fields.ForeignKey(UserProfileResource, "owner", blank=False)
    class Meta:
        filtering = {
                "owner": ALL_WITH_RELATIONS         
        }
        queryset = Cellar.objects.all()
        authorization = Authorization() # TODO: Proper auth

class WineryResource(ModelResource):
    wines = fields.ToManyField("wine.api.WineResource", "wines", null=True)
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
    winery = fields.ForeignKey(WineryResource, "winery", null=True, blank=False, full=True)
    class Meta:
        queryset = Wine.objects.all()
        authorization = Authorization() # TODO: Proper auth
        filtering = {
            "name": ALL
        }

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

    def render_wines(self, wines, request):
        """
            Returns an HTTPResponse object containing a list of wines. If the user
            has passed in the `limit` parameter in their request, this is limited
            to that amount. This returns this list of wines in the order they
            were provided to this method
        """
        rendered_wines = [self.full_dehydrate(self.build_bundle(obj=wine, request=request)) 
                          for wine in wines]
        response = []
        if request.GET.get("limit"):
            limit = int(request.GET["limit"])
            response = Serializer().serialize(rendered_wines[:limit])
        else:
            response = Serializer().serialize(rendered_wines)

        return HttpResponse(response, mimetype="application/json")

class BottleResource(ModelResource):
    wine = fields.ForeignKey(WineResource, "wine", full=True)
    cellar = fields.ForeignKey(CellarResource, "cellar", full=True)
    
    class Meta:
        queryset = Bottle.objects.all()
        authorization = Authorization()
        filtering = {
            "cellar": ALL_WITH_RELATIONS,
            "wine": ALL_WITH_RELATIONS,
        }

    def hydrate(self, bundle):
        """ Convert client-side floating-point price representation into
            the server-side representation """
        bundle = hydrate_price("price", bundle)
        return bundle

    def dehydrate(self, bundle):
        """ Convert server-side integer price representation into
            the client-side floating-point representation """
        bundle = dehydrate_price("price", bundle)
        return bundle

class AnnotationResource(ModelResource):
    bottle = fields.ForeignKey(BottleResource, "bottle")

    class Meta:
        queryset = Annotation.objects.all()
        authorization = Authorization()


class SommelierResource(ModelResource):
    class Meta:
        queryset = Sommelier.objects.all()
        authorization = Authorization() # TODO: Proper auth
        filtering = {
            "wine_type": ALL,
            "pairing": ALL
        }
