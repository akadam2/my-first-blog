from django.shortcuts import render
from .models import Tracks,Artist,Album,Genre

# Create your views here.

def tracks(request):
    tracks = Tracks.objects.all()
    return render(request,'tracks/tracks_list.html', {"tracks":tracks})
