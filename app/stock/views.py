from django.views.generic import ListView, CreateView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import Movimiento
from .serializers import MovimientoSerializer


class ConsumoMedicamentoAPIView(ListView, CreateView):
    pass


class DisponibilidadMedicamentoAPIView(ListView, CreateView):
    pass


class QuiebreStockAPIView(ListView, CreateView):
    pass


class AlertaCaducidadLoteAPIView(ListView, CreateView):
    pass


class MovimientoListCreateView(ListView, CreateView):
    model = Movimiento
    template_name = "movimiento_list.html"
    context_object_name = "movimientos"
    fields = "__all__"


class MovimientoRetrieveDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer


class MovimientoLoteRetrieveView(ListView, CreateView):
    pass


class MovimientoMedicamentoView(ListView, CreateView):
    pass


class ConsumoListCreateView(ListView, CreateView):
    pass


class ConsumoRetrieveDestroyView(ListView, CreateView):
    pass
