from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import videoView, video_list
from video import views

urlpatterns = [
    
    path("home", videoView.as_view(), name="video"),
    path('search',  views.video_list, name="search_video"),
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
