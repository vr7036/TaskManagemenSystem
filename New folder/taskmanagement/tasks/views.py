from django.shortcuts import render
from  .models import TaskAssignment,TaskCategory,Tasks
from .serializers import TaskAssignmentSerializer,TaskCategorySerializer,TaskSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions,viewsets

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Tasks, TaskCategory, TaskAssignment, User


# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset=Tasks.objects.all()
    serializer_class=TaskSerializer
   


class TaskCategoryViewSet(viewsets.ModelViewSet):
    queryset=TaskCategory.objects.all()
    serializer_class=TaskCategorySerializer
    

class TaskAssignmentViewSet(viewsets.ModelViewSet):
    queryset=TaskAssignment.objects.all()
    serializer_class=TaskAssignmentSerializer
    


class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer


# def task_list(request):
#     tasks=Tasks.objects.all().order_by('due_date','priority')
#     content={
#         "tasks":tasks
#     }
#     return render(request,'task_list.html',content)

def task_list(request):
    sort_by=request.GET.get('sort_by','due_date')
    order=request.GET.get('order','asc')
    tasks=Tasks.objects.all()
    if order=='desc':
        sort_by=f'-{sort_by}'
    tasks=tasks.order_by(sort_by)

    status=request.GET.get('status')
    priority=request.GET.get('priority')
    if status:
        tasks=tasks.filter(status=status)
    if priority:
        tasks=tasks.filter(priority=priority)
    return render(request,'task_list.html',{'tasks':tasks})

def task_create(request):
    if request.method=='POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        status=request.POST.get('status')
        priority=request.POST.get('priority')
        due_date=request.POST.get('due_date')
        category_id=request.POST.get('category_id')
        category=TaskCategory.objects.get(id=category_id)

        Tasks.objects.create(
            title=title,
            description=description,
            status=status,
            priority=priority,
            due_date=due_date,
            category=category
        )
        return redirect('task_list')
    categories=TaskCategory.objects.all()
    return render(request,'task_create.html',{'categories':categories})

def task_assign(request):
    if request.method=='POST':
        task_id=request.POST.get('task_id')
        user_id=request.POST.get('user_id')

        task=Tasks.objects.get(id=task_id)
        user=User.objects.get(id=user_id)

        TaskAssignment.objects.create(
            task=task,
            user=user
        )
        
        send_task_notification(user.email,task)
        return redirect('task_list')
    tasks=Tasks.objects.all()
    users=User.objects.all()
    return render(request,'task_assign.html',{'tasks':tasks,'users':users})

def send_task_notification(user_email,task):
    send_mail(
        'New Task Assigned',
        f'You have been assigned a new task:{task.title}',
        'tadisinavishalreddy@gmail.com',
        [user_email],
        fail_silently=False,

    )




