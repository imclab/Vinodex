from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from django.contrib.auth.models import User
from ..models.user import UserProfile
from tastypie import fields

class UserResource(ModelResource):
    profile = fields.ToOneField("wine.api.UserProfileResource", "profile",
                                null=True)
    class Meta:
        resource_name = "auth/user"
        queryset = User.objects.all()
        authorization = Authorization()

class UserProfileResource(ModelResource):
    user = fields.ToOneField(UserResource, "user", blank=False)
    cellars =\
    fields.ToManyField("wine.api.CellarResource","cellars",related_name="owner",
            blank=True)
    class Meta:
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
