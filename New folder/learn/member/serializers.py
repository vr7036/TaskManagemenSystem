from rest_framework import serializers
from member.models import Member
from datetime import date

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Member
        fields= ['id','name','email','Date_of_birth']


