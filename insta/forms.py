from django import forms
from . models import Images,Profile,Comments
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UploadImageForm(forms.ModelForm):
    
    class Meta:
            model = Images
            fields = '__all__'
            exclude = ['profile','likes']
            
            
class ProfilePicForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
 
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
         
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name','body')
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'})
        }