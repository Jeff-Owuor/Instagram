from django.urls import re_path,path
from insta.views import index,imageUpload,updateProfilePage,LikeView

urlpatterns = [
    re_path(r'^$', index , name='home'),
    path('postImage/', imageUpload ,  name='imageUpload'),
    path('updateProfile',updateProfilePage, name='updateProfile'),
    path('like/<int:pk>',LikeView,name='like_post'),
    
]