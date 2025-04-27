from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm, MessageForm
from .utils import paginateProfiles


# Create your views here.

def loginUser(request):
    """
    The view handles login request using
    login template
    """
    page = 'login'
    context = {'page': page}

    if request.user.is_authenticated:
        return redirect('artworks')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are successfully logged in!')
            return redirect('artworks')
        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'artists/login_register.html')


def logoutUser(request):
    """
    The view logs user out and displays
    info message

    """
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')


def registerUser(request):
    """
    The view handles registration request using
    CustomUserCreation form
    """
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('edit-account')

        else:
            messages.error(
                request, 'An error has occurred during registration')

    context = {'page': page, 'form': form}
    return render(request, 'artists/login_register.html', context)


def profiles(request):
    """
    The view displays list of all registered artists
    on the platform and allows search via name and location

    """
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    profiles = Profile.objects.filter(
        Q(name__icontains=search_query) | Q(location__icontains=search_query))

    custom_range, profiles = paginateProfiles(request, profiles, 3)

    context = {
        'profiles': profiles, 'search_query': search_query,
        'custom_range': custom_range}
    return render(request, 'artists/profiles.html', context)


def artistProfile(request, pk):
    """
    The view handles individual artist profile

    """
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'artists/artist_profile.html', context)


@login_required(login_url='login')
def userAccount(request):
    """
    The view displays artist profile info and display artworks
    created by the artists
    """
    profile = request.user.profile
    artworks = profile.artworks_set.all()

    context = {'profile': profile, 'artworks': artworks}
    return render(request, 'artists/account.html', context)


@login_required(login_url='login')
def editAccount(request):
    """
    The view handles editing user account
    """
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your account details are succefssfully edited!')

            return redirect('account')

    context = {'form': form}
    return render(request, 'artists/profile_form.html', context)


@login_required(login_url='login')
def inbox(request):
    """
    The view displays message inbox and shows
    messages sent by registered artists or site visitors

    """
    profile = request.user.profile
    messageRequests = profile.receiver_messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()

    context = {'messageRequests': messageRequests, 'unreadCount': unreadCount}
    return render(request, 'artists/inbox.html', context)


@login_required(login_url='login')
def viewMessage(request, pk):
    """
    The view shows message box displaying message details
    sent by sender

    """
    profile = request.user.profile
    message = profile.receiver_messages.get(id=pk)

    if message.is_read is False:
        message.is_read = True
        message.save()

    context = {'message': message}
    return render(request, 'artists/message.html', context)


def createMessage(request, pk):
    """
    The view allows creation of new message to send to an artist.
    Based on registered or unregisted user, the form displays different fields

    """

    recipient = Profile.objects.get(id=pk)
    form = MessageForm()

    try:
        sender = request.user.profile
    except AttributeError:
        sender = None

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()

            messages.success(request, 'Your message was succefssfully sent!')
            return redirect('artist-profile', pk=recipient.id)

    context = {'recipient': recipient, 'form': form}
    return render(request, 'artists/message_form.html', context)
