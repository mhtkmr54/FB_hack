from django.db import models
from users.models import FBUserProfile
# Create your models here.

class FBPosts(models.Model):
  desc = models.CharField(max_length = 500)
  post_id = models.CharField(max_length = 50)
  link = models.CharField(max_length = 500)
  picture = models.CharField(max_length = 500)
  likes = models.IntegerField(default=0)
  shares = models.IntegerField(default=0)
  likes_given = models.IntegerField(default=0)
  shares_given = models.IntegerField(default=0) 
  created_time = models.DateTimeField()

class shares(models.Model):
  share = models.CharField(max_length = 50)
  post = models.ForeignKey(FBPosts, related_name="post")
  user = models.ForeignKey(FBUserProfile)