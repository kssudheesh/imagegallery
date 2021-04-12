from django.db import models

# Create your models here.

class Picture(models.Model):
    image = models.ImageField(null=False, blank=False)