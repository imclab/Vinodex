from django.conf.urls import patterns, include, url
from wine.api import WineResource, WineryResource, UserResource
from tastypie.api import Api

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(WineResource())
v1_api.register(WineryResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wine.views.home', name='home'),
    # url(r'^wine/', include('wine.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),


    (r'^api/', include (v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
