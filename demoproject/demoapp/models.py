
from django.db import models

# Create your models here.
class Travel(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    description=models.TextField()

    def __str__(self):
        return self.name

class Teams(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pictures')
    description=models.TextField()
