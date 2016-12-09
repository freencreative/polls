#from django.conf.urls.defaults import patterns, url
from django.conf.urls import include, url, patterns

from .forms import RADIUSAuthenticationForm
from users import views

urlpatterns = patterns('django.contrib.auth.views',

#    url(r'^getlogin/$', 'getlogin',
#        name='radius_getlogin'),

    url(r'^login/$', 'login',
        {'authentication_form': RADIUSAuthenticationForm},
        name='radius_login'),

)

#urlpatterns = [
#    url(r'^getlogin/$', views.getlogin, name='getlogin'),
#    url(r'^login/$', views.login, name='radius_login'),
#]
