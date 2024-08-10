# core/urls.py

from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api-auth/", include("rest_framework.urls")),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    # path("maestro/", include("stock.urls")),
    path("stock/", include("stock.urls")),
    # path("inventario", include("inventario.urls")),
]
