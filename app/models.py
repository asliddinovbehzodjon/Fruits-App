from django.db import models

# Create your models here.
class FruitsModel(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='fruits-images')
    cost = models.IntegerField()
    def __str__(self):
        return self.name