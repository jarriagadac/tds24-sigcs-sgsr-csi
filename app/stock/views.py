from django.views.generic import ListView, CreateView, RetrieveUpdateDestroyAPIView
from .models import Movimiento

# Vista para listar y crear movimientos
class MovimientoListCreateView(ListView, CreateView):
    model = Movimiento
    template_name = 'movimiento_list.html'
    context_object_name = 'movimientos'
    fields = '__all__'

# Vista para recuperar y destruir movimientos
class MovimientoRetrieveDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer  # Asegúrate de tener un serializer

# Otras vistas (proporciona una herencia adecuada y evita definir as_view manualmente)
class ConsumoMedicamentoAPIView(ListView, CreateView):
    pass

class DisponibilidadMedicamentoAPIView(ListView, CreateView):
    pass

class QuiebreStockAPIView(ListView, CreateView):
    pass

class AlertaCaducidadLoteAPIView(ListView, CreateView):
    pass

class MovimientoLoteRetrieveView(ListView, CreateView):
    pass

class MovimientoMedicamentoView(ListView, CreateView):
    pass

class ConsumoListCreateView(ListView, CreateView):
    pass

class ConsumoRetrieveDestroyView(ListView, CreateView):
    pass
