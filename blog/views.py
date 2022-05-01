from django.shortcuts import render
from django.utils import timezone
from .models import Post,Sample

# Create your views here.

def index(request):
    posts = Post.objects.filter(title__contains="sample").order_by('create_date')
    return render(request, 'blog/index.html', {'posts':posts})
