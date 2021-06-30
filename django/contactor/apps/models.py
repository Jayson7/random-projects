from django.db import models

# Create your models here.
class Contact(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="Images")
    number = models.PositiveBigIntegerField()

    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name_plural = "Contact"