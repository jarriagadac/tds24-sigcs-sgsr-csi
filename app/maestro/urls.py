from django.urls import path

from .views import (
    InstitucionesRetrieveDestroyAPIView,
    MedicamentosRetrieveDestroyAPIView,
    ItemsRetrieveDestroyAPIView,
    InstitucionesListCreateView,
    ItemsListCreateView,
    MedicamentosListCreateView,
    QuiebreListCreateView,
    QuiebreRetrieveDestroyAPIView,
    EquipamientoListCreateView,
    EquipamientoRetrieveDestroyAPIView,
)

app_name = "maestro"
urlpatterns = [
    path("instituciones", InstitucionesListCreateView.as_view(), name="instituciones-lc"),
    path("instituciones/<int:pk>", InstitucionesRetrieveDestroyAPIView.as_view(), name="instituciones-rud"),
    path("items", ItemsListCreateView.as_view(), name="items-lc"),
    path("items/<int:pk>", ItemsRetrieveDestroyAPIView.as_view(), name="items-rud"),
    path("medicamentos", MedicamentosListCreateView.as_view(), name="medicamentos-lc"),
    path("medicamentos/<int:pk>", MedicamentosRetrieveDestroyAPIView.as_view(), name="medicamentos-rud"),
    path("quiebres", QuiebreListCreateView.as_view(), name="medicamentos-lc"),
    path("quiebres/<int:pk>", QuiebreRetrieveDestroyAPIView.as_view(), name="medicamentos-rud"),
    path("equipamientos", EquipamientoListCreateView.as_view(), name="medicamentos-lc"),
    path("equipamientos/<int:pk>", EquipamientoRetrieveDestroyAPIView.as_view(), name="medicamentos-rud"),
]
