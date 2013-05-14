from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from tastypie import fields
from user import UserProfileResource
from ..models import Cellar

class CellarResource(ModelResource):
    owner = fields.ForeignKey(UserProfileResource, "owner", blank=False)
    class Meta:
        filtering = {
                "owner": ALL_WITH_RELATIONS         
        }
        queryset = Cellar.objects.all()
        authorization = Authorization()
