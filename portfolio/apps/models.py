from django.db import models

# Create your models here.
class App(models.Model):
    project_name = models.CharField(max_length=200)
    link = models.URLField()
    about = models.CharField(max_length=500)
    picture = models.ImageField(upload_to="images")
    github = models.URLField()

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