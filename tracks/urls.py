from django.urls import path
from . import views

app_name = "tracks"
urlpatterns = [
    path('',views.tracks, name="tracks_list"),
    path('tracks/<int:pk>', views.track_details, name = "track_details")
]