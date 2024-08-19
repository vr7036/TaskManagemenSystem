from rest_framework import serializers
from .models import TaskAssignment,TaskCategory,Tasks
from django.contrib.auth.models import User

class TaskCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=TaskCategory
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class TaskSerializer(serializers.ModelSerializer):
 
  
    class Meta:
        model=Tasks
        fields='__all__'

class TaskAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=TaskAssignment
        fields='__all__'
        

