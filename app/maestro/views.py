from rest_framework import generics

from .models import Institucion, Medicamento, Item, Quiebre, Equipamiento
from .serializers import InstitucionSerializer, MedicamentoSerializer, ItemSerializer, QuiebreSerializer, EquipamientoSerializer


class InstitucionesRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer
    http_method_names = ["delete", "get"]


class MedicamentosRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer
    http_method_names = ["delete", "get"]


class ItemsRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    http_method_names = ["delete", "get"]


class QuiebreRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Quiebre.objects.all()
    serializer_class = QuiebreSerializer
    http_method_names = ["delete", "get"]


class EquipamientoRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Equipamiento.objects.all()
    serializer_class = EquipamientoSerializer
    http_method_names = ["delete", "get"]


class InstitucionesListCreateView(generics.ListCreateAPIView):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer
    http_method_names = ["post", "get"]


class ItemsListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    http_method_names = ["post", "get"]


class MedicamentosListCreateView(generics.ListCreateAPIView):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer
    http_method_names = ["post", "get"]


class QuiebreListCreateView(generics.ListCreateAPIView):
    queryset = Quiebre.objects.all()
    serializer_class = QuiebreSerializer
    http_method_names = ["post", "get"]


class EquipamientoListCreateView(generics.ListCreateAPIView):
    queryset = Equipamiento.objects.all()
    serializer_class = EquipamientoSerializer
    http_method_names = ["post", "get"]
