"""
Serializer for Django models
"""

from rest_framework import serializers
from .models import Code


class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = ["icd10_code", "category", "diagnosis"]
