from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import sample

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dynsettings_proj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('^$', sample),
    url(r'^admin/', include(admin.site.urls)),
)
