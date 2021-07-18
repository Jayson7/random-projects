from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from applander import views
from applander.views import homeMainView

urlpatterns = [
    path("contact/", include("contact.urls")),

    path('', views.homeMainView, name="mainhome"),
    path('admin/', admin.site.urls),
    path("audio/", include("audio.urls")),
    path("video/", include("video.urls")),
    path("pdf/", include("pdf.urls")),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)