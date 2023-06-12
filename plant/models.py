from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class regmodel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)    
    address=models.CharField(max_length=100)
    contact=models.CharField(max_length=10)