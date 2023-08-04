from django.db import models

# Create your models here.
class Travelplace(models.Model):
     image=models.ImageField(upload_to='pics')
     name=models.CharField(max_length=250)
     desc=models.TextField()

     def __str__(self):
        return self.name

class Team(models.Model):
     img=models.ImageField(upload_to='pic')
     name=models.CharField(max_length=250)

     def __str__(self):
        return self.name