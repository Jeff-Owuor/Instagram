from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    profile_photo = CloudinaryField('profilePhoto')
    bio = models.TextField(blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()


class Images(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=50)
    image_caption = models.TextField(blank=True)
    profile= models.ForeignKey(Profile,on_delete=models.CASCADE,default=1)
    likes = models.ManyToManyField(User, related_name='instagram')
    
    def num_likes(self):
        return self.likes.count()
    
    @classmethod
    def get_image_by_id(cls,id):
        images = cls.objects.get(id=id)
        return images
    
    @classmethod
    def get_Profile(cls, user):
        profile = Images.objects.filter(user__user=user).all()
        return profile
    
class Comments(models.Model):
    image = models.ForeignKey(Images,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=60)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_added']
        
class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'