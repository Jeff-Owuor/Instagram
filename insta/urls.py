from django.urls import re_path,path
from insta.views import index,imageUpload

urlpatterns = [
    re_path(r'^$', index , name='home'),
    path('postImage/', imageUpload ,  name='imageUpload'),
    
]