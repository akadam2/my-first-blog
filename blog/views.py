from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post,Sample

# Create your views here.

def index(request):
    posts = Post.objects.filter(title__contains="sample").order_by('create_date')
    return render(request, 'blog/index.html', {'posts':posts})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def about(request):
    return render(request, 'blog/about.html')    