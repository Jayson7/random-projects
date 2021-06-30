
from django.contrib import admin
from django.urls import path
from timers import views
from timers.views import home

urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),
]
