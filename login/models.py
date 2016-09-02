from django.db import models
# Create your models here.
class  Users(models.Model):
    User_name=models.CharField(max_length=200)
    User_password=models.CharField(max_length=200)
