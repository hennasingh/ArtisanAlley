from django.shortcuts import render

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
    page = 'Artworks'
    context = {'page': page, 'artworks': artworklist}
    return render(request, 'artworks/artworks.html', context)

def artwork(request, pk):
    artworkObj = None
    for i in artworklist:
        if i['id'] == pk:
            artworkObj = i
    return render(request, 'artworks/single-artwork.html', {'artwork': artworkObj})
