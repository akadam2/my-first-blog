from django.db import models

# Create your models here.
class Horse(models.Model):
    name = models.CharField(max_length=25)
    height = models.DecimalField(max_digits=2,decimal_places=1)
    color = models.TextField(max_length=15)

    def __str__(self):
        return self.name

