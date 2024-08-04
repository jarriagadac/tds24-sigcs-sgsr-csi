import logging
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ConsumoSerializer, MovimientoSerializer
from .models import Movimiento, Consumo

logger = logging.getLogger("myapp")


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


class QuiebreStockAPIView(APIView):
    pass


class AlertaCaducidadLoteAPIView(APIView):
    pass


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
