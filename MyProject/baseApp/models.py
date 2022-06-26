from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=20)
    date_created = models.DateField(auto_now_add=True)