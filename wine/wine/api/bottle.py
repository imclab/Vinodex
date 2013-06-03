from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from cellar import CellarResource
from wine import WineResource
from tastypie import fields
from ..models.bottle import Bottle
from hydration import hydrate_price, dehydrate_price

class BottleResource(ModelResource):
    wine = fields.ForeignKey(WineResource, "wine", full=True)
    cellar = fields.ForeignKey(CellarResource, "cellar", full=True)
    
    class Meta:
        queryset = Bottle.objects.all()
        always_return_data = True
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
