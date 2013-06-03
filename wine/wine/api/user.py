from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.conf.urls import url
from tastypie.utils import trailing_slash
from ..models.user import UserProfile
from ..models.cellar import Cellar
from tastypie import fields
from tastypie.http import HttpUnauthorized, HttpNotFound
from tastypie.exceptions import BadRequest
from django.db import IntegrityError

class UserResource(ModelResource):
    class Meta:
        excludes = ['password']
        resource_name = "auth/user"
        queryset = User.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post']

    def override_urls(self):
        return [
             url(r"^(?P<resource_name>%s)/login%s$" %
                 (self._meta.resource_name, trailing_slash()),
                 self.wrap_view('login'), name="api_login")
             ]

    def login(self, request, **kwargs):
        self.method_check(request, allowed=['post'])

        data = self.deserialize(request, request.raw_post_data, 
                                format=request.META.get('CONTENT_TYPE', 'application/json'))

        username = data.get('username', '')
        password = data.get('password', '')

        users = User.objects.filter(username=username, password=password)

        if users:
            return self.create_response(request, {
                "success":True,
                "userId": users[0].get_profile().id
            })
        else:
            if not User.objects.filter(username=username).exists():
                return self.create_response(request,{
                    'success': False,
                    'reason': 'user does not exist'
                }, HttpNotFound)
            else:
                return self.create_response(request, {
                    'success': False,
                    'reason': 'incorrect',
                    }, HttpUnauthorized )

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


    def obj_update(self, bundle, request=None, **kwargs):
        profile = UserProfile.objects.get(id=kwargs['pk'])
        bundle.obj = profile
        user = profile.user
        if bundle.data.get("name"):
            profile.name = bundle.data["name"]
            profile.save()

        if bundle.data.get("email"):
            user.email = bundle.data["email"]
            user.username = bundle.data["email"]
            user.save()

        if bundle.data.get("password"):
            user.password = bundle.data["password"]
            user.save()

        return bundle
            

    def obj_create(self, bundle, request=None, **kwargs):
        """
            This method is overriden, so that the caller of this method can create
            a UserProfile and User model at the same time. See the documentation 
            on each of the models to see the differences between them.
        """
        if not bundle.data.get("email") and not bundle.data.get("password"):
            # Handle this error condition using the default case
            return super(UserProfileResource, self).obj_create(bundle, **kwargs)
        else:
            # Create the user
            email = bundle.data.get("email")
            password = bundle.data.get("password")

            if User.objects.filter(email=email).exists():
                raise BadRequest("A user with this e-mail already exists")

            user = User.objects.create(email=email, username=email, password=password)


            # Associate a userprofile with the user
            profile = UserProfile.objects.create(name=bundle.data.get("name"),
                                                    user=user)

            # Start the user off with a cellar
            cellar = Cellar.objects.create(name="Default", owner=profile)

            # Return the created profile
            bundle.obj = profile
            return bundle
