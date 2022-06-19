from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    Text = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name='blog_posts')
    Created_on = models.DateTimeField(auto_now = True)
    Published_date = models.DateTimeField(default=timezone.now)
