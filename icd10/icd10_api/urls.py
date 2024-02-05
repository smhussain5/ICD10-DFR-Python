"""
URLS.py file for ICD10_api
"""

from django.urls import path
from .views import AllCodes, SingleCode, UpdateCode, DeleteCode

urlpatterns = [
    path("", AllCodes.as_view()),  # Return ALL ICD-10 codes
    path("<str:icd10_code>/", SingleCode.as_view()),  # Return single ICD-10 code
    path("<str:icd10_code>/update/", UpdateCode.as_view()),  # Update single ICD-10 code
    path("<str:icd10_code>/delete/", DeleteCode.as_view()),  # Delete single ICD-10 code
]
