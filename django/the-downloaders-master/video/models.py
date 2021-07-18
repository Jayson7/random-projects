from django.db import models

# Create your models here.

class Video(models.Model):
    Title = models.CharField(max_length=200)
    File = models.FileField(upload_to="video")
    Image = models.FileField(upload_to="images/video")
    Date_uploaded = models.DateTimeField(auto_now_add=True)
    Info = models.CharField(max_length=500)

    
    def __str__(self):
        return self.Title