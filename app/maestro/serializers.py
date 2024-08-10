from rest_framework import serializers


from .models import Equipamiento, Institucion, Item, Medicamento, Quiebre


class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = [
            "nombre",
            "tipo",
            "titularidad",
            "num_camas_uti",
            "num_camas_uci",
        ]


class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = [
            "nombre_comercial",
            "nombre_generico",
            "ingredientes",
            "concentracion",
            "forma_presentacion",
            "forma_farmaceutica",
            "via_administracion",
            "indicaciones_terapeuticas",
            "contraindicaciones",
            "efectos_secundarios",
            "instrucciones_dosificacion",
            "fabricante",
            "informacion_almacenamiento",
            "interacciones_medicamentosas",
        ]


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            "nombre",
            "tipo",
        ]


class EquipamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipamiento
        fields = [
            "item",
            "marca",
            "modelo",
        ]


class QuiebreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiebre
        fields = ["institucion", "medicamento", "cantidad"]
