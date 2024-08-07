from django.db import models
from datetime import date
from maestro.models import Medicamento, Institucion, Quiebre


class Lote(models.Model):
    codigo = models.CharField(max_length=255)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)
    fecha_vencimiento = models.DateField(default=date.today)
    has_transfer = models.BooleanField(default=False)
    vencido = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.codigo}"


class Consumo(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)
    fecha = models.DateField(default=date.today)

    def __str__(self) -> str:
        return f"{self.institucion} - {self.medicamento} ({self.cantidad}) - fecha: {self.fecha}"


class Stock(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)
    fecha_actualizacion = models.DateField(default=date.today)
    has_quiebre = models.BooleanField(default=False)

    class Meta:
        unique_together = ("institucion", "medicamento")

    def __str__(self) -> str:
        return f"{self.institucion} - {self.medicamento} - faltaMedicamento: {self.has_quiebre}"

    def upd_has_quiebre(self):
        quiebre = Quiebre.objects.filter(institucion=self.institucion, medicamento=self.medicamento).first()
        if quiebre:
            if self.cantidad < quiebre.cantidad:
                self.has_quiebre = True
            else:
                self.has_quiebre = False


class Movimiento(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    lote = models.OneToOneField(Lote, on_delete=models.CASCADE)
    fecha = models.DateField(default=date.today)

    def __str__(self) -> str:
        return f"{self.institucion} - {self.lote.codigo} ({self.lote.cantidad}) - fecha: {self.fecha}"
