from django.conf.urls.defaults import patterns, include, url
        
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
        
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loginsesion.views.home', name='home'),
    # url(r'^loginsesion/', include('loginsesion.foo.urls')),
        
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^regist/$', 'regist.views.regist'),
    url(r'^login/$', 'regist.views.login'),
    url(r'^index/$', 'regist.views.index'),
    url(r'^logout/$', 'regist.views.logout'),
)