from django.urls import path
from . import views
from .views import PostListView, PostDetailView,PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

app_name = 'better_blog'
urlpatterns=[
    path('',PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/',UserPostListView.as_view(), name='user-posts'),
    path('betterpost/<int:pk>/update/',PostUpdateView.as_view(),name='betterpost-update'),
    path('betterpost/<int:pk>/delete/',PostDeleteView.as_view(),name='betterpost-delete'),
    path('betterpost/create/', PostCreateView.as_view(), name="betterpost-create"),
    path('betterpost/<int:pk>/',PostDetailView.as_view(), name="betterpost-detail" ),
    path('about/',views.about, name='blog-about'),
]