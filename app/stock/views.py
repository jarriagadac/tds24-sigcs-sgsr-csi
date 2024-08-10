import logging
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ConsumoSerializer, MovimientoSerializer
from .models import Movimiento, Consumo, Lote, Stock
from datetime import datetime
from maestro.models import Medicamento, Quiebre
from django.core.paginator import Paginator
from django.utils import timezone
from django.shortcuts import render

logger = logging.getLogger("myapp")


class ConsumoMedicamentoAPIView(APIView):
    def get(self, request, medicamento=None):

        if not medicamento:
            medicamentos = Medicamento.objects.all()
        else:
            medicamentos = Medicamento.objects.filter(pk=medicamento)

        data_response = {}

        for medicamento in medicamentos:

            consumos = Consumo.objects.filter(medicamento=medicamento.id)
            # serializer = ConsumoSerializer(consumo, many=True)
            if consumos:
                data_response[medicamento.id] = {"medicamento": medicamento.id, "cantidad": 0, "consumos": []}
                for consumo in consumos:
                    data_response[medicamento.id]["cantidad"] += consumo.cantidad
                    data_response[medicamento.id]["consumos"].append(
                        {"institucion": consumo.institucion.id, "cantidad": consumo.cantidad, "fecha": consumo.fecha}
                    )
        print(data_response)
        return Response(data_response, status=status.HTTP_200_OK)


class DisponibilidadMedicamentoAPIView(APIView):
    def get(self, request, medicamento=None):

        if not medicamento:
            medicamentos = Medicamento.objects.all()
        else:
            medicamentos = Medicamento.objects.filter(pk=medicamento)

        data_response = {}

        for medicamento in medicamentos:

            stocks = Stock.objects.filter(medicamento=medicamento.id)
            # serializer = ConsumoSerializer(consumo, many=True)
            if stocks:
                data_response[medicamento.id] = {"medicamento": medicamento.id, "cantidad": 0, "stocks": []}
                for stock in stocks:
                    data_response[medicamento.id]["cantidad"] += stock.cantidad
                    data_response[medicamento.id]["stocks"].append({"institucion": stock.institucion.id, "cantidad": stock.cantidad})
        print(data_response)
        return Response(data_response, status=status.HTTP_200_OK)


class QuiebreStockAPIView(APIView):
    def get(self, request):

        medicamentos = Medicamento.objects.all()
        data_response = []

        for medicamento in medicamentos:

            stocks = Stock.objects.filter(medicamento=medicamento.id)
            quiebre = Quiebre.objects.filter(medicamento=medicamento.id).first()

            # serializer = ConsumoSerializer(consumo, many=True)
            if stocks:

                for stock in stocks:
                    data_response.append(
                        {
                            "institucion": stock.institucion.id,
                            "medicamento": medicamento.id,
                            "stock": stock.cantidad,
                            "quiebre": quiebre.cantidad,
                        }
                    )
        print(data_response)
        return Response(data_response, status=status.HTTP_200_OK)


class AlertaCaducidadLoteAPIView(APIView):
    def get(self, request):

        lotes = Lote.objects.all()
        data_response = []

        for lote in lotes:
            if lote.fecha_vencimiento <= datetime.now().date():
                data_response.append(
                    {
                        "id": lote.id,
                        "codigo": lote.codigo,
                        "medicamento": lote.medicamento.id,
                        "cantidad": lote.cantidad,
                        "fecha_vencimiento": str(lote.fecha_vencimiento),
                    }
                )

        print(data_response)
        return Response(data_response, status=status.HTTP_200_OK)


class MovimientoListCreateView(APIView):
    def get(self, request):
        movimiento = Movimiento.objects.all()
        serializer = MovimientoSerializer(movimiento, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MovimientoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovimientoRetrieveDestroyView(APIView):
    def get(self, request, pk):
        try:
            movimiento = Movimiento.objects.get(pk=pk)
            serializer = MovimientoSerializer(movimiento)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Movimiento.DoesNotExist:
            raise NotFound(detail="movimiento no encontrado")

    def delete(self, request, pk):
        try:
            movimiento = Movimiento.objects.get(pk=pk)
            movimiento.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Movimiento.DoesNotExist:
            raise NotFound(detail="movimiento no encontrado")


class MovimientoMedicamentoView(APIView):
    def get(self, request, medicamento=None):
        try:
            if medicamento is not None:
                movimiento = Movimiento.objects.prefetch_related("lote__medicamento").filter(lote__medicamento__id=medicamento)
            else:
                movimiento = Movimiento.objects.prefetch_related("lote__medicamento").all()

            if not movimiento.exists():
                return Response([], status=status.HTTP_200_OK)

            movimiento_medicamento = {}

            for row in movimiento:
                medicamento_id = row.lote.medicamento.id

                if medicamento_id not in movimiento_medicamento:
                    movimiento_medicamento[medicamento_id] = {"medicamento": medicamento_id, "movimientos": []}

                movimiento_medicamento[medicamento_id]["movimientos"].append(
                    {"institucion": row.institucion.id, "lote": row.lote.id, "fecha": row.fecha}
                )

            result = list(movimiento_medicamento.values())

            return Response(result, status=status.HTTP_200_OK)
        
        except Exception as e:
            logger.error(f"Error: {e}")
            return Response({"error": "Hubo un problema al obtener los movimientos."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ConsumoListCreateView(APIView):
    def get(self, request):
        consumos = Consumo.objects.all()  # Obtén todos los consumos
        serializer = ConsumoSerializer(consumos, many=True)  # Serializa los datos
        return Response(serializer.data, status=status.HTTP_200_OK)  # Devuelve los datos serializados

    def post(self, request):
        serializer = ConsumoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConsumoRetrieveDestroyView(APIView):
    def get(self, request, pk):
        try:
            consumo = Consumo.objects.get(pk=pk)
            serializer = ConsumoSerializer(consumo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Consumo.DoesNotExist:
            raise NotFound(detail="Consumo no encontrado")

    def delete(self, request, pk):
        try:
            consumo = Consumo.objects.get(pk=pk)
            consumo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Consumo.DoesNotExist:
            raise NotFound(detail="Consumo no encontrado")
        

def lista_movimientos(request):
    movement_list = Movimiento.objects.all()
    paginator = Paginator(movement_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    now = timezone.now()
    context = {
        'movements': page_obj,
        'now': now,
        'page_obj': page_obj,
    }
    return render(request, 'stock/medication_movement_list.html', context)


def lista_caducados(request):
    return render(request, 'stock/caducidad_medicamentos_list.html')

def lista_disponibilidad_medicamentos(request):
    return render(request, 'stock/disponibilidad_medicamentos_list.html')
