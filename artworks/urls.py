from django.urls import path
from . import views

urlpatterns = [
    #making it empty screen results in displaying it on the main page
    path('' , views.artworks, name="artworks"),
    path('artwork/<str:pk>', views.artwork, name="artwork"),

    path('create-artwork/', views.createArtwork, name="create-artwork"),

    path('update-artwork/<str:pk>/', views.updateArtwork, name="update-artwork")
]