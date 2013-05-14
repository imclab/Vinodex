from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from ..models import Sommelier

class SommelierResource(ModelResource):
    class Meta:
        queryset = Sommelier.objects.all()
        authorization = Authorization() 
        filtering = {
            "wine_type": ALL,
            "pairing": ALL
        }
