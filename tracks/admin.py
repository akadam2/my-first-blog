from django.contrib import admin
from .models import Tracks,Artist,Genre,Album

# Register your models here.
admin.site.register(Tracks)
admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Album)

