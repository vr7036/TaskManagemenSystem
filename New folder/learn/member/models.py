from django.db import models

# Create your models here.
class Member(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(null=True,blank=True)
    Date_of_birth=models.DateField(null=True)
    
