from django.contrib import admin
from django.urls import path
from .views import audioView
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import Audio_list

urlpatterns = [
    
    path("home", audioView.as_view(), name="audio"),
    
    path("search", views.Audio_list, name="search_audio"),

   
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
