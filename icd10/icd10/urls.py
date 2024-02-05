"""
URLS.py file for ICD10
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),  # Administration panel
    path("api-auth/", include("rest_framework.urls")),  # Login/Logout
    path("api/", include("icd10_api.urls")),  # API routes
]
