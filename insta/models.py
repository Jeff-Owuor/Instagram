from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Images(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=50)
    image_caption = models.TextField(blank=True)