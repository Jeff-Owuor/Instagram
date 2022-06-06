from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UploadImageForm,ProfilePicForm,CommentForm
from .models import Comments, Images,Profile,Follow
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic import DetailView
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import logout


def unfollow(request, to_unfollow):
    if request.method == 'GET':
        user_profile2 = Profile.objects.get(pk=to_unfollow)
        unfollow_d = Follow.objects.filter(follower=request.user.profile, followed=user_profile2)
        unfollow_d.delete()
        return redirect('profile', user_profile2.user.username)


def follow(request, to_follow):
    if request.method == 'GET':
        user_profile3 = Profile.objects.get(pk=to_follow)
        follow_s = Follow(follower=request.user.profile, followed=user_profile3)
        follow_s.save()
        return redirect('profile', user_profile3.user.username)

def logout_user(request):
    logout(request)
    return redirect('home')

def LikeView(request,pk):
    post = get_object_or_404(Images, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    
    return redirect('home')


def index(request):
    images = Images.objects.all()
    return render(request,'insta/index.html',{'images':images})

class UserEditView(UpdateView):
    form_class= UserChangeForm
    template_name = 'user/user_profile.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user
    
def profile(request, username):
        user_profile = Images.get_Profile(username)
        print(user_profile.username)
        if request.user == user_profile:
           return redirect('update_profile', username=request.user.username)
      
    
        context = {
        'user_profile': user_profile,
       
         }

        return render(request, 'user/user_profile.html', context)


class AddCommentView(CreateView):
    model = Comments
    form_class = CommentForm
    template_name= 'insta/add_comments.html'
    def form_valid(self, form):
        form.instance.image_id = self.kwargs['pk']
        return super().form_valid(form)
    
    success_url = reverse_lazy('home')
    

# Create your views here.
@login_required(login_url='/accounts/login/')
def imageUpload(request):
    current_user  = request.user
    if request.method =='POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('home')
    else:
        form  = UploadImageForm()
        context  = {
            "form":form
            }
    return render(request, 'insta/post.html', context)



@login_required(login_url='/accounts/login/')
def updateProfilePage(request):
   current_user  = request.user
   
   if request.method =='POST':
        form = ProfilePicForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('home')
   else:
        form  = ProfilePicForm()
        context  = {
            "form":form
            }
   return render(request,'user/update_profile.html',context)

# @login_required(login_url='/accounts/login/')
# def myprofile(request, username = None):

#     if not username:
#         username = request.user.username
#     # images by user id
#     images = Images.objects.filter(user_id=username)

#     return render(request, 'myprofile.html', locals())
