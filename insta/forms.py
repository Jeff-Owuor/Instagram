from django import forms
from . models import Images,Profile,Comments


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
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name','body')
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'})
        }