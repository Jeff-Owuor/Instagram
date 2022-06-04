from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UploadImageForm


def index(request):
 
    return render(request,'insta/index.html',{})

# Create your views here.
@login_required(login_url='/accounts/login/')
def imageUpload(request):
    user = request.user
    upload_form = UploadImageForm(instance=user)
    return render(request,'insta/post.html',{'upload_form':upload_form})