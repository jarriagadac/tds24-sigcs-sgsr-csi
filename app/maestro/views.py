from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Institucion, Medicamento, Equipamiento, Quiebre
from .serializers import InstitucionSerializer, MedicamentoSerializer, ItemSerializer, EquipamientoSerializer, QuiebreSerializer


class InstitucionGetCreateView(APIView):
    def get(self, request):
        consumos = Institucion.objects.all()  # Obtén todas las instituciones
        serializer = InstitucionSerializer(consumos, many=True)  # Serializa los datos
        return Response(serializer.data, status=status.HTTP_200_OK)  # Devuelve los datos serializados

    def post(self, request):
        serializer = InstitucionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemGetCreateView(APIView):
    def get(self, request):
        consumos = ItemGetCreateView.objects.all()  # Obtén todas las instituciones
        serializer = ItemSerializer(consumos, many=True)  # Serializa los datos
        return Response(serializer.data, status=status.HTTP_200_OK)  # Devuelve los datos serializados

    def post(self, request):
        serializer = ItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MedicamentoGetCreateView(APIView):
    def get(self, request):
        consumos = Medicamento.objects.all()  # Obtén todas las instituciones
        serializer = MedicamentoSerializer(consumos, many=True)  # Serializa los datos
        return Response(serializer.data, status=status.HTTP_200_OK)  # Devuelve los datos serializados

    def post(self, request):
        serializer = MedicamentoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EquipamientoGetCreateView(APIView):
    def get(self, request):
        consumos = Equipamiento.objects.all()  # Obtén todas las instituciones
        serializer = EquipamientoSerializer(consumos, many=True)  # Serializa los datos
        return Response(serializer.data, status=status.HTTP_200_OK)  # Devuelve los datos serializados

    def post(self, request):
        serializer = EquipamientoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuiebreGetCreateView(APIView):
    def get(self, request):
        consumos = Quiebre.objects.all()  # Obtén todas las instituciones
        serializer = QuiebreSerializer(consumos, many=True)  # Serializa los datos
        return Response(serializer.data, status=status.HTTP_200_OK)  # Devuelve los datos serializados

    def post(self, request):
        serializer = QuiebreSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
