from django.views.generic import ListView, CreateView

from .models import Movimiento


class MovimientoListCreateView(ListView, CreateView):
    model = Movimiento
    template_name = "movimiento_list.html"
    context_object_name = "movimientos"
    fields = "__all__"
