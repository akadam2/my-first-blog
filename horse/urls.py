from django.urls import path
from . import views

app_name = "horse"
urlpatterns=[
    path('',views.HorseListView.as_view(),name="horse_list"),
    path('horse/<int:pk>',views.HorseDetailView.as_view(), name="horse_detail")
]