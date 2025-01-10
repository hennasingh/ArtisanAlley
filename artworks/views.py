from django.shortcuts import render
from .models import Artworks

# Create your views here.

artworklist = [
    {
    'id':'1',
    'title': 'Sunshine Arts',
    'description': 'Acrylic on 10 by 10 canvas'
    
    },
    {
    'id':'2',
    'title': 'Two Souls Jewellery',
    'description': '100% silver jewellery, crafted by hand'
    },
    {
    'id':'3',
    'title': 'Quilled Arts',
    'description': 'Paper coil crafts on 10 by 10 canvas'
    }
]

def artworks(request):
    # this is how we pass messages/variables to html page
    artworks = Artworks.objects.all()
    context = {'artworks': artworks}
    return render(request, 'artworks/artworks.html', context)

def artwork(request, pk):
    artworkObj = Artworks.objects.get(id=pk)
    return render(request, 'artworks/single-artwork.html', {'artwork': artworkObj})
