from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from cloudinary.forms import CloudinaryFileField
from django.contrib.auth.models import User
from .models import Profile, Message


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
        }


class ProfileForm(ModelForm):
    profile_image = CloudinaryFileField()

    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'location', 'bio', 
        'short_intro', 'profile_image', 'social_instagram', 'social_website', 'social_facebook' ]


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']