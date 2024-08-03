from django.db import models
from datetime import date
from maestro.models import Medicamento, Institucion


class Lote(models.Model):
    codigo = models.CharField(max_length=255)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_vencimiento = models.DateField()
    has_transfer = models.BooleanField(default=False)
    vencido = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.codigo}"


class Consumo(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.institucion} - {self.medicamento} ({self.cantidad}) - fecha: {self.fecha}"


class Stock(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)
    fecha_actualizacion = models.DateField(auto_now_add=True)
    has_quiebre = models.BooleanField(default=False)

    class Meta:
        unique_together = ("institucion", "medicamento")

    def __str__(self) -> str:
        return f"{self.institucion} - {self.medicamento} - faltaMedicamento: {self.has_quiebre}"


class Movimiento(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    lote = models.OneToOneField(Lote, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.institucion} - {self.lote.codigo} ({self.lote.cantidad}) - fecha: {self.fecha}"
