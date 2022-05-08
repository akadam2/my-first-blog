from pyexpat import model
from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import Horse

# Create your views here.

class HorseListView(generic.ListView):
    model = Horse

# def horse_details(request,pk):
#     horse = get_object_or_404(Horse,pk=pk)
#     return render(request, 'horse/horse_details.html', {"horse":horse})

class HorseDetailView(generic.DetailView):
    model = Horse
