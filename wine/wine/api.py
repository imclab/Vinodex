from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from wine.models import Wine, Winery

class WineResource(ModelResource):
    class Meta:
        queryset = Wine.objects.all()
        authorization = Authorization() # TODO: Proper auth

class WineryResource(ModelResource):
    class Meta:
        queryset = Winery.objects.all()
        authorization = Authorization() # TODO: Proper auth

