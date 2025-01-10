from django.shortcuts import render
from .models import Artworks
from .forms import ArtworkForm

# Create your views here.

def artworks(request):
    # this is how we pass messages/variables to html page
    artworks = Artworks.objects.all()
    context = {'artworks': artworks}
    return render(request, 'artworks/artworks.html', context)

def artwork(request, pk):
    artworkObj = Artworks.objects.get(id=pk)
    return render(request, 'artworks/single-artwork.html', {'artwork': artworkObj})


def createArtwork(request):
    form = ArtworkForm()
    context = {'form': form}
    return render(request, 'artworks/artwork_form.html', context)
