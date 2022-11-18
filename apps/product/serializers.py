from dataclasses import fields
from statistics import mode
from rest_framework import serializers
from .models import *


class AuthorSerializer(serializers.ModelSerializer):
    f_name = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = '__all__'

    def get_f_name(self, obj):
        return obj.full_name[:4]
