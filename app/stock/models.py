from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from maestro.models import Medicamento, Institucion, Quiebre
from datetime import date


class Lote(models.Model):
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    fecha_vencimiento = models.DateField()
    codigo = models.CharField(max_length=255)
    cantidad = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.codigo


class Consumo(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    fecha = models.DateField(default=date.today)
    cantidad = models.PositiveIntegerField()

    # Cada consumo debe disminuir la cantidad de Stock, y a su vez establecer si hay o no quiebre
    def actualizar_stock(self):
        s = Stock.objects.filter(institucion=self.institucion, medicamento=self.medicamento).first()
        if s:
            s.upd_cantidad()
            s.upd_has_quiebre()


class Stock(models.Model):

    def upd_cantidad(self):
        self.cantidad = 0
        for m in Movimiento.objects.filter(institucion=self.institucion, lote__medicamento=self.medicamento):
            if m.lote.fecha_vencimiento > date.today():
                self.cantidad = self.cantidad + m.lote.cantidad

        for c in Consumo.objects.filter(institucion=self.institucion, medicamento=self.medicamento):
            self.cantidad = self.cantidad - c.cantidad
        self.save()

    def upd_has_quiebre(self):
        q = Quiebre.objects.filter(institucion=self.institucion, medicamento=self.medicamento).first()
        if q:
            if q.cantidad >= self.cantidad:
                self.has_quiebre = True
            else:
                self.has_quiebre = False
            self.save()

    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)
    fecha_actualizacion = models.DateField(default=date.today)
    has_quiebre = models.BooleanField(default=False)

    class Meta:
        unique_together = [("institucion", "medicamento")]


class Movimiento(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    fecha = models.DateField(default=date.today)
    lote = models.OneToOneField(Lote, unique=True, on_delete=models.CASCADE)

    # Cada movimiento debe aumentar la cantidad de Stock, y a su vez establecer si hay o no quiebre
    def actualizar_stock(self):
        s = Stock.objects.filter(institucion=self.institucion, medicamento=self.lote.medicamento).first()
        if s:
            s.upd_cantidad()
            s.upd_has_quiebre()
        return


# Cuando un recurso de movimiento o consumo se crea correctamente, se actualiza el stock (y el campo 'has_quiebre')
@receiver(post_save, sender=Movimiento)
@receiver(post_save, sender=Consumo)
def actualizar_stock_post_save(sender, instance, created, **kwargs):
    if created:
        instance.actualizar_stock()
