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
        r'^accounts/logout/',
        'django.contrib.auth.views.logout',
        name='logout'
    ),
    url(
        r'^redirect_test/',
        'polls.views.redirect_test',
        name='redirect_test'
    ),
]
