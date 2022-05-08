from django.urls import path 
from . import views

app_name = "blog"
urlpatterns = [
    path('',views.index, name = 'blog-home'),
    path('post/<int:pk>/',views.post_detail,name="post-detail"),
    path('about/',views.about, name="blog-about")
]