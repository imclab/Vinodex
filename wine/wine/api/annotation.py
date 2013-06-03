from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from tastypie import fields
from ..models import Annotation
from bottle import BottleResource

class AnnotationResource(ModelResource):
    bottle = fields.ForeignKey(BottleResource, "bottle")

    class Meta:
        queryset = Annotation.objects.all()
        authorization = Authorization()
        filtering = { field:ALL_WITH_RELATIONS for field in
                Annotation._meta.get_all_field_names() }
