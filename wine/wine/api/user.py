from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from django.contrib.auth.models import User
from ..models.user import UserProfile
from tastypie import fields

class UserResource(ModelResource):
    profile = fields.ToOneField("wine.api.UserProfileResource", "profile",
                                null=True)
    class Meta:
        excludes = ['password']
        resource_name = "auth/user"
        queryset = User.objects.all()
        authorization = Authorization()

        def override_urls(self):
            return [
                 url(r"^(?P<resource_name>%s)/login%s$" %
                     (self._meta.resource_name, trailing_slash()),
                     self.wrap_view('login'), name="api_login"),
                 url(r'^(?P<resource_name>%s)/logout%s$' %
                     (self._meta.resource_name, trailing_slash()),
                     self.wrap_view('logout'), name='api_logout'),
                 ]

        def login(self, request, **kwargs):
            self.method_check(request, allowed=['post'])

            data = self.deserialize(request, request.raw_post_data, 
                                    format=request.META.get('CONTENT_TYPE', 'application/json'))

            username = data.get('username', '')
            password = data.get('password', '')

            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return self.create_response(request, {
                        'success': True
                        })
                else:
                    return self.create_response(request, {
                        'success': False,
                        'reason': 'disabled',
                        }, HttpForbidden )
            else:
                return self.create_response(request, {
                    'success': False,
                    'reason': 'incorrect',
                    }, HttpUnauthorized )

        def logout(self, request, **kwargs):
            self.method_check(request, allowed=['get'])
            if request.user and request.user.is_authenticated():
                logout(request)
                return self.create_response(request, { 'success': True })
            else:
                return self.create_response(request, { 'success': False }, HttpUnauthorized)

class UserProfileResource(ModelResource):
    user = fields.ToOneField(UserResource, "user", blank=False, full=True)
    cellars =\
    fields.ToManyField("wine.api.CellarResource","cellars",related_name="owner",
            blank=True)
    class Meta:
        always_return_data = True
        resource_name = "profile"
        queryset = UserProfile.objects.all()
        authorization = Authorization()

    def obj_create(self, bundle, **kwargs):
        """
            This method is overriden, so that the caller of this method can create
            a UserProfile and User model at the same time. See the documentation 
            on each of the models to see the differences between them.
        """
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
