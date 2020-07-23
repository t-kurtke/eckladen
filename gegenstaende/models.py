from django.db import models

# Create your models here.
class Gegenstand(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FilePathField(path="/img")
    status = models.CharField(max_length=100)
    
