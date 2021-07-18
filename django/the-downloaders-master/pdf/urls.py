from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import pdfView, pdf_list
from pdf import views

urlpatterns = [
    
    path("home", pdfView.as_view(), name="pdf"),
    
    path('search',  views.pdf_list, name="search_pdf"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
