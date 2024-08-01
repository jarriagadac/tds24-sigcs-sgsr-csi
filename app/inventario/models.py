from django.db import models
from django.db.models import UniqueConstraint

from maestro.models import Institucion, Equipamiento


class Inventario(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    equipamiento = models.ForeignKey(Equipamiento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    class Meta:
        constraints = [
            UniqueConstraint(fields=["institucion", "equipamiento"], name="unique_institucion_equipamiento"),
        ]
