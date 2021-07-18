from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.
categories = (
        ("Programming","Programming"),
        ("Web Apps", "Web Apps"),
        ("Designs","Designs"),
        ("Cyber Security", "Cyber Security"),
        
    )

class Category(models.Model):
  

    name = models.CharField(choices=categories, default='Web Apps', max_length=120)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

    def __str__(self) -> str:
        return self.name  



class App(models.Model):
    project_name = models.CharField(max_length=200)
    link = models.URLField()
    about = models.CharField(max_length=500)
    picture = CloudinaryField('image')
    github = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'App'
        verbose_name_plural = 'App'

    def __str__(self) -> str:
        return self.project_name  
import django_filters

class AppFilter(django_filters.FilterSet):
    class Meta:
        model = App
        fields = ['project_name']