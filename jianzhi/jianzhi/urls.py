from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jianzhi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^regist/$', 'regist.views.regist'),
    url(r'^login/$', 'regist.views.login'),
    url(r'^index/$', 'regist.views.index'),
    url(r'^logout/$', 'regist.views.logout'),
    )
