from rest_framework import serializers
from .models import Chips

class ChipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chips
        fields = ('id', 'name', 'packaging', 'air_percentage', 'description', 'user')