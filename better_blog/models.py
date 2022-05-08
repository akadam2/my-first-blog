from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 
from django.urls import reverse

# Create your models here.

class BetterPost(models.Model):
    pass

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('better_blog:betterpost-detail',kwargs={'pk':self.pk})       
