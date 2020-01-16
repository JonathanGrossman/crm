from rest_framework import serializers
from data.models import Analysis

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = '__all__'