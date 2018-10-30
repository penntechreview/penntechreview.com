from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title
