from django.conf.urls.defaults import patterns, include, url
#from bp2p.p2p.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'bp2p.p2p.views.index', name='index'),

    url(r'^lista$', 'bp2p.p2p.views.lista', name='lista'),

    # url(r'^bp2p/', include('bp2p.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
