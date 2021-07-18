from .views import contact
from contact import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
urlpatterns = [
    path('contact', views.contact, name="contact"),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
