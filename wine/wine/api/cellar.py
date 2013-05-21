from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from tastypie import fields
from user import UserProfileResource
from ..models import Cellar

class CellarResource(ModelResource):
    owner = fields.ForeignKey(UserProfileResource, "owner", blank=False)
    num_bottles = fields.IntegerField(attribute="num_bottles")
    num_wines = fields.IntegerField(attribute="num_wines")
    class Meta:
        filtering = {
                "owner": ALL_WITH_RELATIONS         
        }
        queryset = Cellar.objects.all()
        authorization = Authorization()
