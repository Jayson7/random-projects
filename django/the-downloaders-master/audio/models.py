from django.db import models

# Create your models here.

class Audio(models.Model):
    Title = models.CharField(max_length=200)
    Artist = models.CharField(max_length=200)
    File = models.FileField(upload_to="audio")
    Album = models.CharField(max_length=50)
    Date_uploaded = models.DateTimeField(auto_now_add=True)
    Info = models.CharField(max_length=500)

    

    
    def __str__(self):
        return self.Title