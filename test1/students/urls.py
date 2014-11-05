from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^$', 'students.views.all'),
    (r'^modify(\d+)/', 'students.views.modify'),
    (r'^delete(\d+)/', 'students.views.delete'),
    (r'^add/', 'students.views.add'),