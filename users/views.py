from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.context import Context, RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from users.forms import *
from users.models import *
from FBHack.likes.models import *
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
import urllib, json
from django.conf import settings
import datetime

def home(request):
  if request.user.is_authenticated():
    users = FBUserProfile.objects.all()
    target = urllib.urlopen('https://graph.facebook.com/Shaastra/posts?limit=50&access_token='+ settings.FACEBOOK_APP_ACCESS_TOKEN).read()
    response = json.loads(target)    
    data = response['data']
    can_like=0
    can_share=0
    for p in data:
      try:
        likes = p['likes']['count']
        can_like=1
      except:
        likes=0
        can_like=0
      try:
        shares = p['shares']['count']
        can_share=1
      except:
        shares=0
        can_share=0
      if not can_like and not can_share :
        continue
      post_id = p['id']
      try:
        desc = p['message']
      except:
        try:
          desc = p['story']
        except:
          try:
            desc = p['caption']
          except:
            desc = p['name']
      link = p.get('link',"http://www.facebook.com/Shaastra")
      try:
        picture = p['picture']
      except:
      	picture = ""
      try:
        old_post = FBPosts.objects.get(post_id=p['id'])
        old_post.likes = likes
        old_post.shares = shares
        old_post.save()
        continue
      except:
        new_post = FBPosts(desc=desc, post_id = post_id, likes=likes, shares=shares, link = link, picture = picture)
        new_post.created_time = datetime.datetime.strptime( p['created_time'][:-5], "%Y-%m-%dT%H:%M:%S" )
        new_post.save()
    posts = FBPosts.objects.all()
    posts=posts.order_by('-id')
    add_form = AddForm()
    #assert False
    return render_to_response('users/home.html', locals(), context_instance=RequestContext(request))  
  return HttpResponseRedirect(settings.SITE_URL + 'login/')

def login(request):
  if request.method=="POST":
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
      auth_login(request, user)
    return HttpResponseRedirect(settings.SITE_URL)
    msg = 'Invalid Username or Password.'
    login_form = LoginForm()
    return render_to_response('users/login.html', locals(), context_instance=RequestContext(request))
  login_form = LoginForm()
  return render_to_response('users/login.html', locals(), context_instance=RequestContext(request))

def register(request):
  return render_to_response('users/register.html', locals(), context_instance=RequestContext(request))

def logout(request):
  auth_logout(request)
  return HttpResponseRedirect(settings.SITE_URL)
