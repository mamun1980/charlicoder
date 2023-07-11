from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import CharliUser


class CharliUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CharliUser
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']