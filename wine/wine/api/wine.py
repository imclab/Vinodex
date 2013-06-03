from winery import WineryResource
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from ..models.wine import Wine
from hydration import hydrate_price, dehydrate_price, dehydrate_raw_data
from tastypie.serializers import Serializer
from django.http import HttpResponse

class WineResource(ModelResource):
    winery = fields.ForeignKey(WineryResource, "winery", null=True, blank=False, full=True)
    class Meta:
        always_return_data = True
        queryset = Wine.objects.all()
        authorization = Authorization() # TODO: Proper auth
        filtering = { 
                "name": ALL_WITH_RELATIONS, 
                "photo": ALL_WITH_RELATIONS, 
                "winery" : ALL_WITH_RELATIONS,
                "vintage" : ALL_WITH_RELATIONS,
                "alcohol_content" : ALL_WITH_RELATIONS,
                "wine_type" : ALL_WITH_RELATIONS,
                "min_price" : ALL_WITH_RELATIONS,
                "max_price" : ALL_WITH_RELATIONS,
                "retail_price" : ALL_WITH_RELATIONS,
                "url" : ALL_WITH_RELATIONS,
                "label_photo" : ALL_WITH_RELATIONS,
                "color" : ALL_WITH_RELATIONS,
                "raw_data" : ALL_WITH_RELATIONS
        }


    def build_filters(self, filters=None):
        if filters is None:
           filters = {}


        for filter in ["min_price", "max_price", "retail_price"]:
            if filter in filters:
                filters[filter] = str(int(float(filters[filter]) * 100.0))

        orm_filters = super(WineResource, self).build_filters(filters)

        return orm_filters
        
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

        if self.get_resource_uri(bundle) == bundle.request.path:
            # Detail call, format the raw data
            bundle = dehydrate_raw_data(bundle)
        else:
            # List call, delete the raw data
            del bundle.data['raw_data']

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
