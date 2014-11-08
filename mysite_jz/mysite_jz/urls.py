from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite_jz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS''
    url(r'^admin/', include(admin.site.urls)),
    url(r'^regist/$','register.views.regist'),
    url(r'^login/$','register.views.login'),
    url(r'^login/regist/$','register.views.regist'),
    url(r'^index/$','register.views.index'),
    url(r'^logout/$','register.views.logout'),
    url(r'^changepassword/(?P<username>\w+)/$','register.views.changepassword'),
    url(r'^personal/$','register.views.personal'),
    url(r'^legalize/$','register.views.legalize'),
    url(r'^school_legalize/$','register.views.school_legalize'),
    url(r'^resume/$','register.views.resume'),
    url(r'^publish/$','register.views.publish'),
    url(r'^school_publish/$','register.views.school_publish'),
    url(r'^forums/', include('forums.urls', namespace='forums')),
#    url(r'^forum/', include('pybb.urls', namespace='pybb')),
)
