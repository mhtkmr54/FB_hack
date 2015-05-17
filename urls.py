from django.conf.urls.defaults import patterns, include, url
from dajaxice.core import dajaxice_autodiscover
dajaxice_autodiscover()
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FBHack.views.home', name='home'),
    # url(r'^FBHack/', include('FBHack.urls')),
    url(r'^', include('users.urls')),
    url(r'^likes/', include('likes.urls')),
    url(r'^facebook/login/?$', 'users.fb_views.login', name = 'fblogin'),
    url(r'^facebook/authentication_callback/?$', 'users.fb_views.authentication_callback', name='fblogin_callback'),
    url(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url('', include('social.apps.django_app.urls', namespace='social')),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)