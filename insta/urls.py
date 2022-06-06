from django.urls import re_path,path
from insta.views import index,imageUpload,updateProfilePage,LikeView,AddCommentView,UserEditView,unfollow,follow,logout_user

urlpatterns = [
    re_path(r'^$', index , name='home'),
    path('post/', imageUpload ,  name='imageUpload'),
    path('updateProfile',updateProfilePage, name='updateProfile'),
    path('like/<int:pk>',LikeView,name='like_post'),
    path('post/<int:pk>/add_comment',AddCommentView.as_view(), name='add_comment'),
    path('user_profile/',UserEditView.as_view(), name='user_profile'),
    path('unfollow/<to_unfollow>',unfollow, name='unfollow'),
    path('follow/<to_follow>', follow, name='follow'),
    path('logout_user/',logout_user,name='logout')
    
]