from django.urls import path
from django.contrib import admin
from .views import sample

urlpatterns = [
    path('', sample),
    path('admin/', admin.site.urls),
]