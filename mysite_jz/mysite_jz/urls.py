from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite_jz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^regist/$','register.views.regist'),
    url(r'^login/$','register.views.login'),
    url(r'^login/regist/$','register.views.regist'),
    url(r'^index/$','register.views.index'),
    url(r'^logout/$','register.views.logout'),
    url(r'^changepassword/(?P<username>\w+)/$','register.views.changepassword'),
    url(r'^personal/$','register.views.personal'),
)
