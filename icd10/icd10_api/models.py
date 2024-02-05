"""
Models for ICD-10 API. Includes models for diagnoses and diagnosis categories
"""

from django.db import models

# Create your models here.


class Code(models.Model):
    """
    Model for ICD-10 diagnoses
    """

    icd10_code = models.CharField(max_length=3, verbose_name="ICD-10 Code")
    category = models.CharField(max_length=1000, verbose_name="ICD-10 Category")
    diagnosis = models.CharField(max_length=1000, verbose_name="ICD-10 Diagnosis")

    class Meta:
        """
        Display verbose plural name in Admin panel
        """

        verbose_name_plural = "ICD-10 Codes"

    def __str__(self):
        return f"{self.icd10_code}: {self.diagnosis}"
