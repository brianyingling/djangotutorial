from django.conf.urls import patterns, include, url
from django.contrib   import admin
from helloworld.views import *
from books.views import *
from contact.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^hello/$', hello),
    ('^home/$', home),
    ('^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    ('^$',home),
    (r'^admin/', include(admin.site.urls)),
    (r'^search-form/$', search_form),
    (r'^search/$', search),
    (r'^contact/$', contact),






    # Examples:
    # url(r'^$', 'helloworld.views.home', name='home'),
    # url(r'^helloworld/', include('helloworld.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
