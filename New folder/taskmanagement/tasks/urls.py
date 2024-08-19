from django.urls import path,include

from rest_framework import routers

from .views import TaskViewSet,TaskAssignmentViewSet,TaskCategoryViewSet,UserViewSet,task_list,task_create,task_assign

router=routers.DefaultRouter()
router.register(r'tasks',TaskViewSet)
router.register(r'categories',TaskCategoryViewSet)
router.register(r'assignments',TaskAssignmentViewSet)
router.register(r'users',UserViewSet)

urlpatterns=[
    path('api/',include(router.urls)),
    path('api-auth',include('rest_framework.urls',namespace='rest_framework')),
    path('tasks/', task_list, name='task_list'),
    path('tasks/create/', task_create, name='task_create'),
    path('tasks/assign/', task_assign, name='task_assign'),


]