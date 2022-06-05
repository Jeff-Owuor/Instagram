from django import forms
from . models import Images,Profile


class UploadImageForm(forms.ModelForm):
    
    class Meta:
            model = Images
            fields = '__all__'
            exclude = ['user']
            
            
class ProfilePicForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']