from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    profile_photo = CloudinaryField('profilePhoto')
    bio = models.TextField(blank=True)

class Images(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=50)
    image_caption = models.TextField(blank=True)
    profile= models.ForeignKey(Profile,on_delete=models.CASCADE,default=0)