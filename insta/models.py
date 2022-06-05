from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    profile_photo = CloudinaryField('profilePhoto')
    bio = models.TextField(blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} Profile'

class Images(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=50)
    image_caption = models.TextField(blank=True)
    profile= models.ForeignKey(Profile,on_delete=models.CASCADE,default=1)
    likes = models.ManyToManyField(User, related_name='instagram')
    
    def num_likes(self):
        return self.likes.count()