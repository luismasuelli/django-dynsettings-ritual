from django.conf.urls import include, url
from django.contrib import admin
from .views import sample

urlpatterns = [
    url('^$', sample),
    url(r'^admin/', include(admin.site.urls)),
]