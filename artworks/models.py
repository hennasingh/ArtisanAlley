from django.db import models
import uuid
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from . import choices
from artists.models import Profile

# Create your models here.


class Artworks(models.Model):
    """
    Stores a single artwork entry related to :model:`artists.Profile`
    and :model: 'artworks.Tag`.

    """

    profile_owner = models.ForeignKey(
        Profile, null=True, blank=True,
        on_delete=models.SET_NULL
    )
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
    listing_image1 = CloudinaryField('image', blank=True, null=True)
    listing_image2 = CloudinaryField('image', blank=True, null=True)
    listing_image3 = CloudinaryField('image', blank=True, null=True)
    price = models.IntegerField()
    town = models.CharField(max_length=100)
    county = models.CharField(max_length=100, choices=choices.COUNTIES)
    art_medium = models.CharField(max_length=50)
    tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True,
        editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


class Tag(models.Model):
    """
    Stores a single tag
    """
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True,
        editable=False)

    def __str__(self):
        return self.name