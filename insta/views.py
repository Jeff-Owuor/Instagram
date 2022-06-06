from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from .forms import UploadImageForm,ProfilePicForm,CommentForm
from .models import Comments, Images
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


def LikeView(request,pk):
    post = get_object_or_404(Images, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    
    return redirect('home')


def index(request):
    images = Images.objects.all()
    return render(request,'insta/index.html',{'images':images})

class AddCommentView(CreateView):
    model = Comments
    form_class = CommentForm
    template_name= 'insta/add_comments.html'
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
