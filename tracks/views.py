from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def tracks(request):
    return HttpResponse("<h1>Welcome to tracks</h1>")
