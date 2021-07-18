from django.db import models

# Create your models here.

class pdf(models.Model):
    Title = models.CharField(max_length=200)
    Author = models.CharField(max_length=200)
    File = models.FileField(upload_to="pdf")
    Date_uplaoded = models.DateTimeField(auto_now_add=True)
  


    
    def __str__(self):
        return self.Title