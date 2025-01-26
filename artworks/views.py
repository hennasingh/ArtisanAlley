from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cloudinary.forms import cl_init_js_callbacks  
from .models import Artworks
from .forms import ArtworkForm
from .utils import paginateArtworks

# Create your views here.

def artworks(request):
    """
    Renders the most recent artworks on the website and allows viewing 
    artists profile.
    Displays an individual instance of :model:`artworks.Artworks`
    and handles pagination
    """
    artworks = Artworks.objects.all()

    custom_range, artworks = paginateArtworks(request, artworks, 6)

    context = {'artworks': artworks, 'custom_range':custom_range}
    return render(request, 'artworks/artworks.html', context)


def artwork(request, pk):
    """
    The view handles display of details in a single artwork piece
    """
    artworkObj = Artworks.objects.get(id=pk)
    return render(request, 'artworks/single-artwork.html', {'artwork': artworkObj})


@login_required(login_url="login")
def createArtwork(request):
    """
    The view handles creation of new artwork via ArtworkForm
    """
    profile = request.user.profile
    form = ArtworkForm()

    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.profile_owner = profile
            artwork.save()
            messages.success(request, 'Artwork was created successfully!')
            return redirect('account')

    context = {'form': form}
    return render(request, 'artworks/artwork_form.html', context)


@login_required(login_url="login")
def updateArtwork(request, pk):
    """
    The view handles update of any artwork piece via Artwork form
    """
    profile = request.user.profile
    artwork = profile.artworks_set.get(id=pk)
    form = ArtworkForm(instance=artwork)

    if request.method == 'POST':
        form = ArtworkForm(request.POST, instance=artwork)
        if form.is_valid():
            form.save()
            messages.success(request, 'Artwork was updated successfully!')
            return redirect('account')

    context = {'form': form}
    return render(request, 'artworks/artwork_form.html', context)


@login_required(login_url="login")
def deleteArtwork(request, pk):
    """
    The view handles delete request of any artwork and confirm 
    deletion using delete-artwork template
    """
    profile = request.user.profile
    artwork = profile.artworks_set.get(id=pk)
    if request.method == 'POST':
        artwork.delete()
        messages.success(request, 'Artwork was deleted successfully!')
        return redirect('account')
    context = {'object': artwork}
    return render(request, 'artworks/delete_artwork.html', context)
