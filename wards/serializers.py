from rest_framework import serializers
from .models import Project
from users.models import Profile


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project


        fields = '__all__'



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile

        fields=['__all__'] 