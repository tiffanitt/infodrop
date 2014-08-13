from django.conf.urls import patterns, include, url

from django.contrib import admin
from tastypie.api import Api
from infoshare.api.resources import UserResource, MediaResource

admin.autodiscover()
v1_api = Api(api_name="v1")
v1_api.register(UserResource())
v1_api.register(MediaResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'infodrop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
