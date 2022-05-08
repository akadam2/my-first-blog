from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from .models import Tracks,Artist,Album,Genre
from django.views import generic

# Create your views here.

def tracks(request):
    tracks = Tracks.objects.all()
    context = 499
    return render(request,'tracks/tracks_list.html', {'tracks':tracks, 'context':context})
 

def track_details(request, pk):
    track = get_object_or_404(Tracks, pk=pk)
    return render(request, "tracks/track_details.html", {"track":track})
