from django.shortcuts import render
from .models import Profile

# Create your views here.
def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'artists/profiles.html', context)


def artistProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile':profile}
    return render(request, 'artists/artist-profile.html', context)