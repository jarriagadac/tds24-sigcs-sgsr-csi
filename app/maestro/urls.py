from django.urls import path

from .views import (
    InstitucionGetCreateView,
    MedicamentoGetCreateView,
    ItemGetCreateView,
    EquipamientoGetCreateView,
    QuiebreGetCreateView,
)

app_name = "maestro"
urlpatterns = [
    path("instituciones", InstitucionGetCreateView.as_view(), name="institucion-lc"),
    path("medicamentos", MedicamentoGetCreateView.as_view(), name="medicamento-lc"),
    path("items", ItemGetCreateView.as_view(), name="item-lc"),
    path("equipamientos", EquipamientoGetCreateView.as_view(), name="equipamiento-lc"),
    path("quiebres", QuiebreGetCreateView.as_view(), name="quiebre-lc"),
]
