from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
#    url(r'^users/', include('users.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

#from django.contrib.staticfiles.views import serve

urlpatterns += staticfiles_urlpatterns()
#def static_khpark(prefix=None):
#	prefix = settings.STATIC_URL
#	return static(prefix, view='django.contrib.staticfiles.views.serve')

#urlpatterns += static_khpark()
