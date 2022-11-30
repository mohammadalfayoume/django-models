from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Snack(models.Model):
    name= models.CharField(max_length=64)
    purchaser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    description  = models.TextField(default="this is descreption")
    
    def __str__(self):
        return self.name # to add names to the snacks in data base