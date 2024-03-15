import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField
from cloudinary.models import CloudinaryField

class UserModel(models.Model) :
    id= models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    avatar = CloudinaryField('image',blank=True)
    first_name=models.CharField(max_length=50 )
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=40,unique=True)
    password=models.CharField( max_length=100)
    role=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    subscription=models.CharField(max_length=10,default='free-tier')
    interests=ArrayField(
            models.CharField(max_length=30)
        )
    ad_preference=ArrayField(
            models.CharField(max_length=30)
        )



