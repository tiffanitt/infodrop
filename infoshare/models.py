from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

def get_pic(instance, filename):
    return 'uploaded_pics/{}'.format(str(filename).replace(' ', '_'))


class User(AbstractUser):

    def __unicode__(self):
        pass


class Media(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User, related_name='user')
    pic = models.FileField(upload_to=get_pic, null=True)

    def __unicode__(self):
        return self.name


