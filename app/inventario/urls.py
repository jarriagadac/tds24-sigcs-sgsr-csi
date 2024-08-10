from django.urls import path

app_name = "inventario"
urlpatterns = [
    path("movimientos", True, name="movimiento-lc"),
]
