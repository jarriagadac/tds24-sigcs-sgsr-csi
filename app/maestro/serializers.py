from rest_framework import serializers


from .models import Institucion, Medicamento


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


class ItemSerializer:
    pass


class EquipamientoSerializer:
    pass


class QuiebreSerializer:
    pass
