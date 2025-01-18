from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.

def loginUser(request):
    page ='login'
    context = {'page': page}

    if request.user.is_authenticated:
        return redirect('artworks')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('artworks')
        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'artists/login_register.html')


def logoutUser(request):
    logout(request)
    messages.success(request, 'User was logged out!')
    return redirect('login')


def registerUser(request):
    page ='register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('profiles')

        else:
            messages.error(request, 'An error has occurred during registration')

    context = {'page': page, 'form':form}
    return render(request,'artists/login_register.html', context )

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'artists/profiles.html', context)


def artistProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile':profile}
    return render(request, 'artists/artist-profile.html', context)