from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy,reverse
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from requests import request
from .models import BetterPost 
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

def home(request):
    posts = BetterPost.objects.all()
    context = {'posts':posts}
    return render(request, 'better_blog/home.html', context)

class PostListView(ListView):
    model = BetterPost
    template_name = 'better_blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = BetterPost
    template_name = 'better_blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return BetterPost.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = BetterPost    

class PostCreateView(CreateView):
    model = BetterPost
    fields = ['title','content']

    success_url = reverse_lazy('better_blog:blog-home')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = BetterPost
    fields = ['title','content']

    # success_url = reverse_lazy('better_blog:blog-home')  
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False        

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = BetterPost
    # fields = ['title','content']

    success_url = reverse_lazy('better_blog:blog-home')  
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 


def about(request):
    return render(request, 'better_blog/about.html')    