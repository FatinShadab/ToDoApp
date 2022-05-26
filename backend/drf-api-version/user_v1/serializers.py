from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """This inherited class define the api representation for User model"""
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']