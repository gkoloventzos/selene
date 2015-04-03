from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'selene.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^walk/','walk'),
    url(r'^walk/(?P<pk>[0-9]+)$','walk_that'),
    url(r'^turn_left/','turn_left'),
    url(r'^turn_right/','turn_right'),
    url(r'^u_turn/','u_turn'),
    url(r'^turn/(?P<pk>[0-9]+)$','turn'),
]
