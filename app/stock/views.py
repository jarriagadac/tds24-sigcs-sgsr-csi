from django.views.generic import ListView
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Movimiento, Consumo, Stock, Quiebre, Lote
from .serializers import MovimientoSerializer, ConsumoSerializer, MovimientoReadSerializer, StockSerializer, LoteSerializer
from datetime import datetime, date


class MovimientoListCreateView(generics.ListCreateAPIView):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer
    http_method_names = ["post", "get"]


class MovimientoRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer
    http_method_names = ["delete", "get"]


class MovimientoLoteRetrieveView:
    pass


class MovimientoMedicamentoView(generics.ListAPIView):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoReadSerializer
    http_method_names = ["get"]

    def get_queryset(self, data):
        queryset = Movimiento.objects.all()
        if data and data["medicamento"]:
            queryset = Movimiento.objects.filter(lote__medicamento=data["medicamento"])
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset(kwargs)
        data = self.get_serializer(queryset, many=True).data
        response = self.process_response(data)
        return Response(response, status=status.HTTP_200_OK)

    def process_response(self, data):
        response = {}
        for m in data:
            medicamento = m["lote"]["medicamento"]
            lote_id = m["lote"]["id"]
            fecha_datetime = datetime.strptime(m.get("fecha"), "%Y-%m-%d").date()
            del m["id"]
            m["lote"] = lote_id
            m["institucion"] = m["institucion"]
            m["fecha"] = fecha_datetime
            if medicamento in response:
                response[medicamento]["medicamento"] = medicamento
                response[medicamento]["movimientos"].append(m)
            else:
                movimientos_list = [m]
                response[medicamento] = {"medicamento": medicamento, "movimientos": movimientos_list}
        return list(response.values())


class ConsumoListCreateView(generics.ListCreateAPIView):
    queryset = Consumo.objects.all()
    serializer_class = ConsumoSerializer
    http_method_names = ["post", "get"]


class ConsumoRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Consumo.objects.all()
    serializer_class = ConsumoSerializer
    http_method_names = ["delete", "get"]


class ConsumoMedicamentoAPIView(generics.ListAPIView):
    queryset = Consumo.objects.all()
    serializer_class = ConsumoSerializer
    http_method_names = ["get"]

    def get_queryset(self, data):
        queryset = Consumo.objects.all()
        if data and data["medicamento"]:
            queryset = Consumo.objects.filter(medicamento=data["medicamento"])
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset(kwargs)
        data = self.get_serializer(queryset, many=True).data
        response = self.process_response(data)
        return Response(response, status=status.HTTP_200_OK)

    def process_response(self, data):
        response = {}
        for c in data:
            medicamento = c.get("medicamento")
            cantidad = c.get("cantidad")
            fecha_datetime = datetime.strptime(c.get("fecha"), "%Y-%m-%d").date()
            del c["id"]
            del c["medicamento"]
            c["fecha"] = fecha_datetime
            consumo_list = list()
            consumo_list.append(c)
            if medicamento in response:
                response[medicamento]["cantidad"] += cantidad
                response[medicamento]["consumos"].append(c)
            else:
                consumo_list = [c]
                response[medicamento] = {"medicamento": medicamento, "cantidad": cantidad, "consumos": consumo_list}
        return response


class DisponibilidadMedicamentoAPIView(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    http_method_names = ["get"]

    def get_queryset(self, data):
        queryset = Stock.objects.all()
        if data and data["medicamento"]:
            queryset = Stock.objects.filter(medicamento=data["medicamento"])
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset(kwargs)
        data = self.get_serializer(queryset, many=True).data
        response = self.process_response(data)
        return Response(response, status=status.HTTP_200_OK)

    def process_response(self, data):
        response = {}
        for s in data:
            medicamento = s.get("medicamento")
            cantidad = s.get("cantidad")
            del s["id"]
            del s["medicamento"]
            del s["has_quiebre"]
            del s["fecha_actualizacion"]
            stocks_list = []
            stocks_list.append(s)
            if medicamento in response:
                response[medicamento]["cantidad"] += cantidad
                response[medicamento]["stocks"].append(s)
            else:
                response[medicamento] = {"medicamento": medicamento, "cantidad": cantidad, "stocks": stocks_list}
        return response


class QuiebreStockAPIView(generics.ListAPIView):
    queryset = Stock.objects.filter(has_quiebre=True)
    serializer_class = StockSerializer
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = self.get_serializer(queryset, many=True).data
        response = self.process_response(data)
        return Response(response, status=status.HTTP_200_OK)

    def process_response(self, data):
        response = []
        for s in data:
            current_value = {}
            institucion = s.get("institucion")
            medicamento = s.get("medicamento")
            stock = s.get("cantidad")
            quiebre = Quiebre.objects.filter(institucion=s.get("institucion"), medicamento=s.get("medicamento")).first()
            quiebre = quiebre.cantidad
            current_value = {"institucion": institucion, "medicamento": medicamento, "stock": stock, "quiebre": quiebre}
            response.append(current_value)
        return response


class AlertaCaducidadLoteAPIView(generics.ListAPIView):
    queryset = Lote.objects.filter(fecha_vencimiento__lt=date.today())
    serializer_class = LoteSerializer
    http_method_names = ["get"]


class MovimientoMedicamentoListView(ListView):
    model = Movimiento
    template_name = "movimientos_medicamentos_graph.html"
    context_object_name = "historico_movimientos"

    def get_queryset(self):
        queryset = Movimiento.objects.all()
        return MovimientoReadSerializer(queryset, many=True).data
