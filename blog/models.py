"""This program creates a class called Post that describes the variables
and methods of each blog Post object. Each blog post has a title, body, 
signature and date."""

from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=140)
    body = models.TextField()
    signature = models.CharField(max_length=140, default="Carissa Moodley")
    date = models.DateTimeField()

def __str__(self):
    return self.title


