from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TaskCategory(models.Model):
    name=models.CharField(max_length=20,null=False)
    description=models.TextField()

class Tasks(models.Model):
    STATUS_CHOICES=[
        ('pending','Pending'),
        ('completed','Completed'),
        ('in_progress','In Progress'),
    ]
    PRIORITY_CHOICES=[
        ('low','Low'),
        ('high','High'),
        ('medium','Medium'),
    ]
    title=models.CharField(max_length=20)
    description=models.TextField()
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
    priority=models.CharField(max_length=20,choices=PRIORITY_CHOICES,default='medium')
    due_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(TaskCategory,on_delete=models.CASCADE)


class TaskAssignment(models.Model):
    task=models.ForeignKey(Tasks,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    assigned_at=models.DateTimeField(auto_now_add=True)




