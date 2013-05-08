from django.conf.urls import patterns, include, url
from registration.forms import RegistrationFormUniqueEmail
from wine.api import (WineResource, WineryResource, UserResource,
                     UserProfileResource, CellarResource)
from tastypie.api import Api

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(WineResource())
v1_api.register(WineryResource())
v1_api.register(UserProfileResource())
v1_api.register(CellarResource())

urlpatterns = patterns('',
    url(r'^$', 'wine.views.home', name='home'),

    # This is just a hack for now, all user pages will redirect to 
    # home. TODO: Actually implement this
    url(r'^users/*', 'wine.views.home', name='home'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'api/v1/wine/ocr', 'wine.views.wine_ocr', name='wine_ocr'),
    # url(r'^wine/', include('wine.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),


    (r'^api/', include (v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
