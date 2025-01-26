from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from cloudinary.forms import CloudinaryFileField
from django.forms import ModelForm
from .models import Profile, Message


class CustomUserCreationForm(UserCreationForm):
    """
    The class defines custom user creation form on user registration
    """
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
        }


class ProfileForm(ModelForm):
    """
    The class defines Profile form that reflects on artist
    account

    """
    profile_image = CloudinaryFileField()

    class Meta:
        model = Profile
        fields = [
            'name', 'email', 'username', 'location', 'bio',
            'short_intro', 'profile_image', 'social_instagram',
            'social_website', 'social_facebook'
        ]


class MessageForm(ModelForm):
    """
    The class defines fields for sending a message
    to an artist

    """
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']
