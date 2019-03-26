from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image, Profile, Comment

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['Likes', 'pub_date', 'Profile']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name']

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['image_name', 'pub_date','profile','user']
        # widgets = {
        #     'likes': forms.CheckboxSelectMultiple(),