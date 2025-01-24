from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile, Message
from .forms import CustomUserCreationForm, ProfileForm
from .utils import paginateProfiles
from django.db.models import Q

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
    messages.info(request, 'User was logged out!')
    return redirect('login')


def registerUser(request):
    page ='register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('edit-account')

        else:
            messages.error(request, 'An error has occurred during registration')

    context = {'page': page, 'form':form}
    return render(request,'artists/login_register.html', context )

def profiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    profiles = Profile.objects.filter( Q (name__icontains=search_query) | Q(location__icontains=search_query))

    custom_range, profiles = paginateProfiles(request, profiles, 3)

    context = {'profiles': profiles, 'search_query': search_query, 'custom_range':custom_range}
    return render(request, 'artists/profiles.html', context)


def artistProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile':profile}
    return render(request, 'artists/artist_profile.html', context)


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    artworks = profile.artworks_set.all()

    context = {'profile':profile, 'artworks': artworks}
    return render(request, 'artists/account.html', context)


@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'artists/profile_form.html', context)


@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    messageRequests = profile.receiver_messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()

    context = {'messageRequests': messageRequests, 'unreadCount': unreadCount}
    return render(request, 'artists/inbox.html', context)


@login_required(login_url='login')
def viewMessage(request, pk):
    profile = request.user.profile
    message = profile.receiver_messages.get(id=pk)

    if message.is_read == False:
        message.is_read = True
        message.save()

    context={'message': message}
    return render(request, 'artists/message.html', context)
