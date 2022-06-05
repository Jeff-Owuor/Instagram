from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UploadImageForm,ProfilePicForm
from .models import Images


def index(request):
    images = Images.objects.all()
    return render(request,'insta/index.html',{'images':images})

# Create your views here.
@login_required(login_url='/accounts/login/')
def imageUpload(request):
    user = request.user
    upload_form = UploadImageForm(instance=user)
    return render(request,'insta/post.html',{'upload_form':upload_form})

@login_required(login_url='/accounts/login/')
def updateProfilePage(request):
    user= request.user
    form = ProfilePicForm(instance=user)
    return render(request,'user/update_profile.html',{"form":form})

# @login_required(login_url='/accounts/login/')
# def myprofile(request, username = None):

#     if not username:
#         username = request.user.username
#     # images by user id
#     images = Images.objects.filter(user_id=username)

#     return render(request, 'myprofile.html', locals())
