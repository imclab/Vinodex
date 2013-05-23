from winery import WineryResource
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from ..models.wine import Wine
from hydration import hydrate_price, dehydrate_price

class WineResource(ModelResource):
    winery = fields.ForeignKey(WineryResource, "winery", null=True, blank=False, full=True)
    class Meta:
        always_return_data = True
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
