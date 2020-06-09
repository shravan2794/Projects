from rest_framework import serializers
from .models import Register,Student,Sign,Session

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields='__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

class SignSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sign
        fields='__all__'

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Session
        fields='__all__'

