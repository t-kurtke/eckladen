from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.category

class Post(models.Model):
    def __str__(self):
        return str(self.title)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, default=1)
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    def get_images(self):
        return PostImage.objects.filter(post=self)

    @property
    def short_body(self):
        return (str(self.body)[:50] + '...') if len(str(self.body)) > 50 else str(self.body)

class PostImage(models.Model):
    image = models.ImageField(upload_to="img/")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Comment(models.Model):
    def __str__(self):
        return  (str(self.body)[:75] + '...') if len(str(self.body)) > 75 else str(self.body)
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)