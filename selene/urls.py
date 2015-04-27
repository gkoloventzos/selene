from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'selene.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^walk/','selene.views.walk',name='walk'),
    url(r'^wwalk/','selene.views.wwalk',name='wwalk'),
    url(r'^walk/(?P<pk>[0-9]+)$','selene.views.walk_that',name='walk_that'),
    url(r'^walk_left/','selene.views.walk_left',name='walk_left'),
    url(r'^wlak_right/','selene.views.walk_right',name='walk_right'),
    url(r'^u_turn/','selene.views.u_turn',name='u_turn'),
    url(r'^turn/(?P<pk>[0-9]+)$','selene.views.turn',name='turn'),
]
