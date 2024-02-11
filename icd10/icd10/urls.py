"""
URLS.py file for ICD10
"""

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),  # Administration panel
    path("api-auth/", include("rest_framework.urls")),  # Login/Logout
    path("api/", include("icd10_api.urls")),  # API routes
    path("api/schema", SpectacularAPIView.as_view(), name="api_schema"),
    path("api/docs", SpectacularSwaggerView.as_view(url_name="api_schema"), name="api_docs"),
]
