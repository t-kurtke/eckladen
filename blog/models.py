from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    def __str__(self):
        return str(self.title)

    title = models.CharField(max_length=250)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    @property
    def short_body(self):
        return (str(self.body)[:50] + '...') if len(str(self.body)) > 50 else str(self.body)

class Comment(models.Model):
    def __str__(self):
        return  (str(self.body)[:75] + '...') if len(str(self.body)) > 75 else str(self.body)
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)