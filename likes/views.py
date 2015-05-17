from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.context import Context, RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
import urllib, json, cgi
from django.conf import settings
from FBHack.likes.models import *

def likes(request):
  responses = []
  if request.method=="POST":
    try:
      likes = int(request.POST.get("likes"))
    except:
      likes = 0
    try:
      shars = int(request.POST.get("shares"))
    except:
      shars = 0
    pid = request.POST.get("pid",0)
    post = FBPosts.objects.get(id=pid)
    users = FBUserProfile.objects.all().order_by('likes_used')
    target = urllib.urlopen('https://graph.facebook.com/' + post.post_id + '/likes?fields=id&limit=1000').read()
    response = json.loads(target)['data']
    liked_by = [x['id'] for x in response]
    shared_by = [s.user for s in shares.objects.filter(post = post)]
    like_by=[]
    cntl = 0
    cnts = 0
    for user in users :
      if user.facebook_id not in liked_by and cntl<likes:
        data = {'access_token': user.access_token,}
        response = urllib.urlopen('https://graph.facebook.com/' + post.post_id + '/likes',urllib.urlencode(data)).read()
        responses.append(response)
        try:
          if response == 'true' :
            cntl = cntl + 1
            like_by.append(user.facebook_id)
            user.likes_used = user.likes_used + 1
            user.active = True
            user.save()
        except:
          user.active = False
          user.save()
    post.likes_given = post.likes_given + cntl
    post.save()
    users = FBUserProfile.objects.all().order_by('shares_used')
    for user in users :
      if cnts<shars and user not in shared_by:
        data = {'link': post.link,
                'picture': post.picture,
                'access_token': user.access_token,}
        response = urllib.urlopen('https://graph.facebook.com/' + user.facebook_id + '/feed',urllib.urlencode(data)).read()
        response = json.loads(response)
        try:
          response['id'] 
          cnts = cnts + 1
          share = shares(post = post, user = user, share = response['id'])
          share.save()
          user.shares_used = user.shares_used + 1
          user.active = True
          user.save()
        except :
          user.active = False
          user.save()
    post.shares_given = post.shares_given + cnts
    post.save()
    #assert False
    return HttpResponse(responses)  
  return HttpResponseRedirect(settings.SITE_URL)