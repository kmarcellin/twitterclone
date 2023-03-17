from django.db import models
from cloudinary.models import CloudinaryField

class Post(models.Model):
    class Meta(object):
        db_table= 'post'

    name = models.CharField(
        'Name',blank=False, null=False, max_length=24, db_index=True,default='Anonymous'
    )

    body = models.CharField(
        'body',blank=False,null=False,max_length=216, db_index=True
    )

    created_at = models.DateTimeField(
         'created_at', blank=True, auto_now_add=True
    )

    image = CloudinaryField(
        'image', blank=True,
    )

    likes= models.PositiveIntegerField(
        'Likes', default=0, null=True, blank=True
    )

    demo = models.CharField(
        'Demo', default='N/A', blank=True, null=True, max_length=30
    )



