from django.conf.urls import patterns, include, url
from registration.forms import RegistrationFormUniqueEmail
from wine.api import (WineResource, WineryResource, UserResource,
                     UserProfileResource, CellarResource, SommelierResource,
                     BottleResource, AnnotationResource)
from tastypie.api import Api

from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(WineResource())
v1_api.register(WineryResource())
v1_api.register(UserProfileResource())
v1_api.register(CellarResource())
v1_api.register(SommelierResource())
v1_api.register(BottleResource())
v1_api.register(AnnotationResource())

urlpatterns = patterns('',
    url(r'^$', 'wine.views.home', name='home'),
    url(r'api/v1/wine/ocr', 'wine.views.wine_ocr', name='wine_ocr'),
    url(r'api/v1/wine/barcode', 'wine.views.wine_barcode', name='wine_barcode'),
    url(r'^wine/image', 'wine.views.upload_image', name='wine_upload_image'),
    url(r'^api/v1/forgotpassword', 'wine.views.forgot_password', name =
        'forgot_password'),
    url(r'^api/v1/passwordreset', 'wine.views.reset_password', name =
        'password_reset'),
    (r'^api/', include (v1_api.urls)),
)
