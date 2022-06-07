from django.urls import re_path,path
from insta.views import index,edit,loginPage,register,imageUpload,updateProfilePage,LikeView,AddCommentView,profile,unfollow,follow,logout_user,user_profile

urlpatterns = [
    re_path(r'^$', index , name='home'),
    path('post/', imageUpload ,  name='imageUpload'),
    path('profile/<int:id>/', profile, name="profile"),
    path('edit/<int:id>/',edit, name="edit"),
    path('register/', register, name='register'),
    path('login/', loginPage, name='login'),
    path('updateProfile',updateProfilePage, name='updateProfile'),
    path('like/<int:pk>',LikeView,name='like_post'),
    path('post/<int:pk>/add_comment',AddCommentView.as_view(), name='add_comment'),
    re_path(r'^user_profile/<username>/$',user_profile, name='user_profile'),
    path('unfollow/<to_unfollow>',unfollow, name='unfollow'),
    path('follow/<to_follow>', follow, name='follow'),
    path('logout_user/',logout_user,name='logout')
    
]