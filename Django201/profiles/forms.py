from django import forms
from django.contrib.auth.models import User
from .models import Profile



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username',
                  'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bg_image']
        labels = {
            'image': 'Avatar',
            'bg_image': 'Background img'
        }