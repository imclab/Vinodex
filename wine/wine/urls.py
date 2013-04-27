from django.conf.urls import patterns, include, url
from wine.api import WineResource, WineryResource

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

wine_resource = WineResource()
winery_resource = WineryResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wine.views.home', name='home'),
    # url(r'^wine/', include('wine.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^api/', include (wine_resource.urls)),
    (r'^api/', include (winery_resource.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
