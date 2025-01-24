from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Artworks
from django.contrib import messages
from .forms import ArtworkForm
from cloudinary.forms import cl_init_js_callbacks  

# Create your views here.

def artworks(request):
    # this is how we pass messages/variables to html page
    artworks = Artworks.objects.all()
    context = {'artworks': artworks}
    return render(request, 'artworks/artworks.html', context)

def artwork(request, pk):
    artworkObj = Artworks.objects.get(id=pk)
    return render(request, 'artworks/single-artwork.html', {'artwork': artworkObj})

@login_required(login_url="login")
def createArtwork(request):
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
    profile = request.user.profile
    artwork = profile.artworks_set.get(id=pk)
    if request.method == 'POST':
        artwork.delete()
        messages.success(request, 'Artwork was deleted successfully!')
        return redirect('account')
    context = {'object': artwork}
    return render(request, 'artworks/delete_artwork.html', context)
