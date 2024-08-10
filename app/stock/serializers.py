from rest_framework import serializers

from .models import Stock, Lote, Consumo, Movimiento


class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = ["id", "codigo", "medicamento", "cantidad", "fecha_vencimiento"]


class ConsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumo
        fields = ["id", "institucion", "medicamento", "cantidad", "fecha"]


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ["id", "institucion", "medicamento", "cantidad", "has_quiebre", "fecha_actualizacion"]

    def get_unique_together_validators(self):
        """Se sobreescribe el metodo, para eliminar la validacion de 'unique_together'"""
        return []


class MovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimiento
        fields = ["id", "institucion", "lote", "fecha"]


class MovimientoReadSerializer(serializers.ModelSerializer):
    lote = LoteSerializer()

    class Meta:
        model = Movimiento
        fields = ["id", "institucion", "lote", "fecha"]
