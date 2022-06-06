from django.urls import re_path,path
from insta.views import index,imageUpload,updateProfilePage,LikeView,AddCommentView,UserEditView

urlpatterns = [
    re_path(r'^$', index , name='home'),
    path('post/', imageUpload ,  name='imageUpload'),
    path('updateProfile',updateProfilePage, name='updateProfile'),
    path('like/<int:pk>',LikeView,name='like_post'),
    path('post/<int:pk>/add_comment',AddCommentView.as_view(), name='add_comment'),
    path('user_profile/',UserEditView.as_view(), name='user_profile')
    
]