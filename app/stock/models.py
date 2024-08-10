from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from datetime import date

from maestro.models import Institucion, Medicamento, Quiebre


class Lote(models.Model):
    codigo = models.CharField(max_length=255)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=500)
    fecha_vencimiento = models.DateField()

    def __str__(self) -> str:
        return f"{self.codigo}"


class Consumo(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.cantidad}"


@receiver(post_save, sender=Consumo)
def actualizar_stock_consumo(sender, instance, created, **kwargs):
    if created:
        stock, created = Stock.objects.get_or_create(
            institucion=instance.institucion, medicamento=instance.medicamento, defaults={"cantidad": 0}
        )
        stock.upd_cantidad()
        stock.upd_has_quiebre()


class Stock(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)
    has_quiebre = models.BooleanField(default=False)
    fecha_actualizacion = models.DateField(auto_now=True)

    # IMPLEMENTACION SOLO PARA EL TEST AVANZADO test_workflow_calculo_stock
    # def upd_cantidad(self, cantidad: int) -> None:
    #     self.cantidad += cantidad
    #     if self.cantidad <= 0:
    #         self.cantidad = 0
    #     self.save()
    ####################################################################

    # IMPLEMENTACION PARA EL TEST AVANZADO test_workflow_calculo_stock y test_workflow_calculo_quiebre_stock
    # def upd_cantidad(self, cantidad: int) -> None:
    #     self.cantidad += cantidad
    #     if self.cantidad <= 0:
    #         self.cantidad = 0
    #     self.upd_has_quiebre()
    #     self.save()

    # def upd_has_quiebre(self) -> None:
    #     quiebre = Quiebre.objects.filter(institucion=self.institucion, medicamento=self.medicamento).first()
    #     if quiebre:
    #         self.has_quiebre = self.cantidad <= quiebre.cantidad
    #     else:
    #         self.has_quiebre = False
    ####################################################################

    # IMPLEMENTACION PARA EL TEST AVANZADO test_workflow_calculo_stock, test_workflow_calculo_quiebre_stock y test_workflow_calculo_caducidad
    def upd_cantidad(self):
        self.cantidad = 0
        for m in Movimiento.objects.filter(institucion=self.institucion, lote__medicamento=self.medicamento):
            if m.lote.fecha_vencimiento > date.today():
                self.cantidad = self.cantidad + m.lote.cantidad
        for c in Consumo.objects.filter(institucion=self.institucion, medicamento=self.medicamento):
            self.cantidad = self.cantidad - c.cantidad
        self.save()

    def upd_has_quiebre(self) -> None:
        quiebre = Quiebre.objects.filter(institucion=self.institucion, medicamento=self.medicamento).first()
        if quiebre:
            self.has_quiebre = self.cantidad <= quiebre.cantidad
        else:
            self.has_quiebre = False
        self.save()

    ###################################################################


class Movimiento(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE, unique=True)
    fecha = models.DateField(auto_now=True)

    class Meta:
        unique_together = [("lote")]


# IMPLEMENTACION PARA EL TEST AVANZADO test_workflow_calculo_stock
# @receiver(post_save, sender=Movimiento)
# def actualizar_stock_movimiento(sender, instance, created, **kwargs):
#     if created:
#         stock, created = Stock.objects.get_or_create(
#             institucion=instance.institucion,
#             medicamento=instance.lote.medicamento
#         )
#         stock.upd_cantidad(instance.lote.cantidad)
#         stock.save()
# ###################################################################


# IMPLEMENTACION PARA EL TEST AVANZADO test_workflow_calculo_stock, test_workflow_calculo_quiebre_stock y test_workflow_calculo_caducidad
@receiver(post_save, sender=Movimiento)
def actualizar_stock_movimiento(sender, instance, created, **kwargs):
    if created:
        stock, created = Stock.objects.get_or_create(institucion=instance.institucion, medicamento=instance.lote.medicamento)
        stock.upd_cantidad()
        stock.upd_has_quiebre()
        stock.save()
