from django.shortcuts import render
from rest_framework import generics
from django.views.generic import TemplateView
from .models import Member
from .serializers import MemberSerializer

class MemberListView(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberTemplateView(TemplateView):
    template_name = 'member_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = Member.objects.all()
        return context
