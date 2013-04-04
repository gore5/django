from django.conf.urls import patterns, include, url
from isobres.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', mainpage, name='home'),
    url(r'^user/(\w+)/$', userpage),
    url(r'^login/$','django.contrib.auth.views.login'),
    #url(r'^$', 'sobres.views.home', name='home'),
    #url(r'^sobres/', include('sobres.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)



