from django.shortcuts import render, redirect
from .models import Artworks
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


def createArtwork(request):
    form = ArtworkForm()

    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('artworks')

    context = {'form': form}
    return render(request, 'artworks/artwork_form.html', context)


def updateArtwork(request, pk):
    artwork = Artworks.objects.get(id=pk)
    form = ArtworkForm(instance=artwork)

    if request.method == 'POST':
        form = ArtworkForm(request.POST, instance=artwork)
        if form.is_valid():
            form.save()
            return redirect('artworks')

    context = {'form': form}
    return render(request, 'artworks/artwork_form.html', context)


def deleteArtwork(request, pk):
    artwork = Artworks.objects.get(id=pk)
    if request.method == 'POST':
        artwork.delete()
        return redirect('artworks')
    context = {'object': artwork}
    return render(request, 'artworks/delete_template.html', context)
