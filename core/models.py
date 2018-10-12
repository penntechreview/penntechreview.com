from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TeamMember(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, primary_key=True)

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title