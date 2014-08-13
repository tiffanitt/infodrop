from tastypie.authorization import Authorization

__author__ = 'TTruong'

from tastypie.resources import ModelResource
from infoshare.models import *

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = "user"
        allowed_methods = ['get', 'post', 'put', 'delete']
        fields = ['first_name', 'last_name', 'username']
        authorization = Authorization()
        always_return_data=True

class MediaResource(ModelResource):
    class Meta:
        queryset = Media.objects.all()
        resource_name = "media"
        allowed_methods = ['get', 'post', 'put', 'delete']
        fields = ['name', 'user', 'pic']
        authorization = Authorization()
        always_return_data=True
