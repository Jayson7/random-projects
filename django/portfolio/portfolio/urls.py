
from django.contrib import admin
from django.urls import path
from apps import views
from apps.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path('search', views.Searchlist, name="search"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

