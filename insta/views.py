from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .forms import UploadImageForm,ProfilePicForm,CommentForm
from .models import Comments, Images,Profile,Follow
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic import DetailView
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate

@login_required(login_url='login')
def unfollow(request, to_unfollow):
    if request.method == 'GET':
        user_profile2 = Profile.objects.get(pk=to_unfollow)
        unfollow_d = Follow.objects.filter(follower=request.user.profile, followed=user_profile2)
        unfollow_d.delete()
        return redirect('profile', user_profile2.user.id)


@login_required(login_url='login')
def follow(request, to_follow):
    if request.method == 'GET':
        user_profile3 = Profile.objects.get(pk=to_follow)
        follow_s = Follow(follower=request.user.profile, followed=user_profile3)
        follow_s.save()
        return redirect('profile', user_profile3.user.id)

@login_required(login_url='login')
def search_profile(request):
    if 'search_user' in request.GET and request.GET['search_user']:
        name = request.GET.get("search_user")
        results = Profile.search_profile(name)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'insta/results.html', params)
    else:
        message = "You haven't searched for any image category"
    return render(request, 'instagram/results.html', {'message': message})

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    return render(request, 'registration/register.html', {"form":form})

def loginPage(request):
    context ={}
    
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
    
    return render(request,'registration/login.html',context)

@login_required(login_url='login/')
def profile(request, id):
    profile = Profile.objects.get(user=id)
    userid = request.user.id
    user_posts = profile.images_set.all()
    followers = Follow.objects.filter(followed=profile)
    follow_status = None
    
    for follower in followers:
        if request.user.profile == follower.follower:
            follow_status = True
        else:
            follow_status = False
    context={
        "profile":profile,
        "userid":userid,
        'user_posts': user_posts,
        'followers': followers,
        'follow_status': follow_status
    }
    return render(request, 'insta/user_profile.html',context)

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login/')
def LikeView(request,pk):
    post = get_object_or_404(Images, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    
    return redirect('home')

@login_required(login_url='login/')
def edit(request, id):
    profile = Profile.objects.get(id=id)
    form = ProfilePicForm(instance=profile)
    userid = request.user.id
    if request.method == "POST":
        form = ProfilePicForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            
            instance.save()
            return redirect(f'profile/{userid}/')
    return render(request, 'insta/edit.html', {"form":form})


def index(request):
    images = Images.objects.all()
    return render(request,'insta/index.html',{'images':images})

class UserEditView(UpdateView):
    form_class= UserChangeForm
    template_name = 'user/user_profile.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user
    
class AddCommentView(CreateView):
    model = Comments
    form_class = CommentForm
    template_name= 'insta/add_comments.html'
    def form_valid(self, form):
        form.instance.image_id = self.kwargs['pk']
        return super().form_valid(form)
    
    success_url = reverse_lazy('home')
    

# Create your views here.
@login_required(login_url='login/')
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
   return render(request,'insta/update_profile.html',context)
