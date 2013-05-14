from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from bottle import BottleResource
from tastypie import fields
from ..models import Annotation

class AnnotationResource(ModelResource):
    bottle = fields.ForeignKey(BottleResource, "bottle")

    class Meta:
        queryset = Annotation.objects.all()
        authorization = Authorization()
