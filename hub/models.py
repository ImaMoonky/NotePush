from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
# Here we are going to make a post class for our project
class Post(models.Model): # Each class will be its own table
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE) # This means that when user is deleted that the post is deleted

    # We want to add a dunder str so that we can gain more data later on
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk })
    # reverse returns full path as a string


