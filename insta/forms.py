from django import forms
from . models import Images


class UploadImageForm(forms.ModelForm):
    
    class Meta:
            model = Images
            fields = '__all__'
            exclude = ['profile']