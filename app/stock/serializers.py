from rest_framework import serializers
from .models import Consumo, Lote, Stock, Movimiento


class ConsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumo
        fields = ["id", "institucion", "medicamento", "cantidad", "fecha"]
        read_only_fields = ["fecha"]


class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = ["id", "codigo", "medicamento", "cantidad", "fecha_vencimiento"]


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ["id", "institucion", "medicamento", "cantidad", "has_quiebre", "fecha_actualizacion"]

    def validate(self, attrs):
        if Stock.objects.filter(institucion=attrs['institucion'], medicamento=attrs['medicamento']).exists():
            raise serializers.ValidationError("La combinación de institucion y medicamento ya existe.")
        return attrs
    
class MovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimiento
        fields = ["id", "institucion", "lote", "fecha"]

