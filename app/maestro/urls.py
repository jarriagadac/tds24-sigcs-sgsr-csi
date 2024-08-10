from django.urls import path

from .views import (
    MovimientoListCreateView,
)

app_name = "maestro"
urlpatterns = [
    path("movimientos", MovimientoListCreateView.as_view(), name="movimiento-lc"),
]
