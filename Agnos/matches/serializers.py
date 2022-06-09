from rest_framework import serializers
from .models import match
class matchSerializer(serializers.ModelSerializer):
    class Meta:
        model = match
        fields = ['message','pattern']




