from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^accounts/login/',
        'django.contrib.auth.views.login',
        name='login',
        kwargs={
            'template_name': 'login.html'
        }
    ),
    url(
        r'^accounts/logoutr/',
        'django.contrib.auth.views.logout',
        name='logout', kwargs={
                'next_page':'/django/polls/accounts/login/'
        }
    ),
    url(
        r'^redirect_test/',
        'polls.views.redirect_test',
        name='redirect_test'
    ),
    url(
        r'^redirect1/',
        'polls.views.redirect1',
        name='redirect1'
    ),
    url(
        r'^redirect2/',
        'polls.views.redirect2',
        name='redirect2'
    ),
    url(
        r'^successlogin/',
        'polls.views.successlogin',
        name='successlogin'
    ),
    url(
        r'^querystring/',
        'polls.views.querystring',
        name='querystring'
    ),
]
