from django.forms import ModelForm, widgets
from django import forms
from cloudinary.forms import CloudinaryFileField
from .models import Artworks


class ArtworkForm(ModelForm):
    """
    The class defines Artwork form for create and edit
    artworks
    """
    featured_image = CloudinaryFileField()
    listing_image1 = CloudinaryFileField()
    listing_image2 = CloudinaryFileField()
    listing_image3 = CloudinaryFileField()

    class Meta:
        model = Artworks
        fields = [
            'title', 'description', 'featured_image',
            'listing_image1', 'listing_image2', 'listing_image3',
            'price', 'town', 'county', 'art_medium', 'tags'
        ]
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
