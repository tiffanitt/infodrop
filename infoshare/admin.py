from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from infoshare.models import Media

admin.site.register(User)
admin.site.register(Media)

