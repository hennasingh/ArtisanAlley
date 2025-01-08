from django.db import models
import uuid
from django.contrib.auth.models import User
from . import choices

# Create your models here.

class Artworks(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    town = models.CharField(max_length=100)
    county = models.CharField(max_length=100, choices=choices.COUNTIES)
    art_medium = models.CharField(max_length=50)
    tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    
    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

