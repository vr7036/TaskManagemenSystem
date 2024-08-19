from django.urls import path
from .views import MemberListView, MemberDetailView,MemberTemplateView

urlpatterns = [
    path('template/members/', MemberTemplateView.as_view(), name='member-list-template'),  # Template view
    path('members/', MemberListView.as_view(), name='member-list'),
    path('members/<int:pk>/', MemberDetailView.as_view(), name='member-detail'),
]
