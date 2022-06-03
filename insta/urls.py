from django.urls import re_path,path
from insta.views import index

urlpatterns = [
    re_path(r'^$',index,name='home'),
    
]