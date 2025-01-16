from django.forms import ModelForm, widgets
from django import forms
from cloudinary.forms import CloudinaryFileField
from .models import Artworks

class ArtworkForm(ModelForm):
    featured_image = CloudinaryFileField()
    listing_image1 = CloudinaryFileField()
    listing_image2 = CloudinaryFileField()
    listing_image3 = CloudinaryFileField()

    class Meta:
        model = Artworks
        fields = ['title', 'description', 'featured_image', 'listing_image1', 'listing_image2', 'listing_image3', 
        'price', 'town', 'county', 'art_medium', 'tags']
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ArtworkForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

