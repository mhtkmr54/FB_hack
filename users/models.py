from django.db import models

class FBUserProfile(models.Model):
  name = models.CharField(max_length=50)
  facebook_id = models.CharField(max_length=20)
  access_token = models.CharField(max_length=250)
  active = models.BooleanField(default = True)
  likes_used = models.IntegerField(default=0)
  shares_used = models.IntegerField(default=0)

  def __unicode__(self):
    return self.name

  class Admin:
    pass