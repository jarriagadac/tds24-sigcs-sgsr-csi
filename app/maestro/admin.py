from django.contrib import admin

from .models import Institucion, Medicamento, Equipamiento, Item, Quiebre


@admin.register(Institucion)
class InstitucionAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "tipo",
        "titularidad",
        "num_camas_uti",
        "num_camas_uci",
        "factor",
    )


@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre_comercial",
        "nombre_generico",
        "forma_presentacion",
        "forma_farmaceutica",
        "via_administracion",
        "fabricante",
    )


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "tipo",
    )


@admin.register(Equipamiento)
class EquipamientoAdmin(admin.ModelAdmin):
    list_display = (
        "modelo",
        "marca",
        "item",
    )


@admin.register(Quiebre)
class QuiebreAdmin(admin.ModelAdmin):
    list_display = (
        "institucion",
        "medicamento",
        "cantidad",
    )
