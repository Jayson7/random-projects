
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from apps import views 
from apps.views import ContactView, contactCreate, contactdetail, contactUpdate, contactDelete, contacthome
router = routers.DefaultRouter()
router.register(r'contact', views.ContactView, 'contact')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', views.contacthome, name="home"),
    path('detail/<str:pk>/', views.contactdetail, name="detail"),
    path('create', views.contactCreate, name="create"),
    path('update/<str:pk>/', views.contactUpdate, name="update"),
    path('delete/<str:pk>/', views.contactDelete, name="delete"),
    
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)