"""
Serializer for Django models
"""

from rest_framework import serializers
from .models import Code


class CodeSerializer(serializers.ModelSerializer):

    # def create(self, validated_data):
    #     return Code.objects.create(**validated_data)
    #
    # def destroy(self):
    #     return Code.objects.destroy()

    class Meta:
        model = Code
        fields = ["icd10_code", "category", "diagnosis"]
