from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Gegenstand(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, default=1)
    is_draft = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="img/")
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
