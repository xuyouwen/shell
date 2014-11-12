from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.views.generic.simple import direct_to_template
from django.views.generic.base import TemplateView
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
    url(r'^index_login/$','register.views.index_login'),
    url(r'^logout/$','register.views.logout'),
#    url(r'^ch_password/(?P<username>\w+)/$','register.views.ch_password'),
    url(r'^ch_password/$','register.views.ch_password'),
    url(r'^personal/$','register.views.personal'),
    url(r'^legalize/$','register.views.legalize'),
    url(r'^school_legalize/$','register.views.school_legalize'),
    url(r'^resume/$','register.views.resume'),
    url(r'^publish/$','register.views.publish'),
    url(r'^school_publish/$','register.views.school_publish'),
    url(r'^business_center/$','register.views.business_center'),
    url(r'^Campus_community/$','register.views.Campus_community'),
    url(r'^personal/$','register.views.personal'),
    url(r'^forums/', include('forums.urls', namespace='forums')),
#    url(r'^index_login/$', TemplateView.as_view(template_name='index_login.html'),('^index_login/(w+)/$')),
#    url(r'^index_login/$',direct_to_template, {'template': 'index_login.html'}),
#    url(r'^forum/', include('pybb.urls', namespace='pybb')),
#    url( r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.STATIC_ROOT }),
)
#if settings.DEBUG:
#        urlpatterns += patterns('django.contrib.staticfiles.views',
#                        url(r'^static/(?P<path>.*)$', 'serve'),
#                            )
