from django.forms import ModelForm
from .models import Artworks

class ArtworkForm(ModelForm):
    class Meta:
        model = Artworks
        fields = '__all__' 