from django.db import models


class Institucion(models.Model):
    class Tipo(models.TextChoices):
        # privada
        CLINICA = "clinica", "Clínica"
        CENTRO_MEDICO = "centro_medico", "Centro Médico"
        HOSPITAL_CLINICO = "hospital_clinico", "Hospital Clínico"
        # secundaria
        HOSPITAL = "hospital", "Hospital"
        # primaria
        CES = "ces", "Centro de Salud"
        CESFAM = "cesfam", "Centro de Salud Familiar"
        CECOSF = "cecosf", "Centro Comunitario de Salud Familiar"
        PSR = "psr", "Postas Salud Rural"
        SAPU = "sapu", "Servicio de Atención Primaria de Urgencia"
        SAR = "sar", "Servicio de Atención Primaria de Urgencia de Alta Resolutividad"
        BODEGA = "bodega", "Bodega"
        FARMACIA = "farmacia", "Farmacia"

    class Titularidad(models.TextChoices):
        PUBLICO = "publico", "Público"
        PRIVADO = "privado", "Privado"

    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=20, choices=Tipo.choices)
    titularidad = models.CharField(max_length=20, choices=Titularidad.choices)
    num_camas_uti = models.PositiveSmallIntegerField(verbose_name="Número de Camas UTI")
    num_camas_uci = models.PositiveSmallIntegerField(verbose_name="Número de Camas UCI")
    factor = models.FloatField(help_text="Factor")

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name_plural = "Instituciones"


class Medicamento(models.Model):
    class Via(models.TextChoices):
        ORAL = "oral", "Oral"
        TOPICA = "topica", "Tópica"
        INTRAVENOSO = "intravenoso", "Intravenoso"
        INTRAMUSCULAR = "intramuscular", "Intramuscular"

    class FormaPresentacion(models.TextChoices):
        FRASCO = "frasco", "Frasco"
        BLISTER = "blister", "Blister"
        AMPOLLA = "ampolla", "Ampolla"

    class FormaFarmaceutica(models.TextChoices):
        TABLETAS = "tabletas", "Tabletas"
        CAPSULAS = "capsulas", "Cápsulas"
        SOLUCION = "solucion", "Solucion"
        CREMA = "crema", "Crema"

    nombre_comercial = models.CharField(max_length=255)
    nombre_generico = models.CharField(max_length=255, null=True, blank=True)
    ingredientes = models.CharField(max_length=255, help_text="Ingredientes químicos o sustancias activas presentes.")
    concentracion = models.CharField(max_length=255, help_text="Cantidad de sustancia activa presente en cada unidad.")
    forma_presentacion = models.CharField(max_length=16, choices=FormaPresentacion.choices)
    forma_farmaceutica = models.CharField(max_length=16, choices=FormaFarmaceutica.choices)
    via_administracion = models.CharField(max_length=16, choices=Via.choices)
    indicaciones_terapeuticas = models.CharField(
        max_length=255, null=True, blank=True, help_text="Condiciones o enfermedades para las cuales se prescribe."
    )
    contraindicaciones = models.CharField(max_length=255, null=True, blank=True)
    efectos_secundarios = models.CharField(max_length=255, null=True, blank=True)
    instrucciones_dosificacion = models.CharField(max_length=255, null=True, blank=True)
    fabricante = models.CharField(max_length=255)
    informacion_almacenamiento = models.CharField(max_length=255, null=True, blank=True)
    interacciones_medicamentosas = models.CharField(
        max_length=255, null=True, blank=True, help_text="Interacciones conocidas con otros medicamentos o sustencias."
    )

    def __str__(self) -> str:
        return f"{self.nombre_comercial} ({self.nombre_generico}) | {self.fabricante}"


class Item(models.Model):
    class Tipo(models.TextChoices):
        SOPORTE_VITAL = "soporte_vital", "Soporte Vital"
        APOYO_MONITORIZACION = "apoyo_monitorizacion", "Apoyo y Monitorización"

    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=32, choices=Tipo.choices)

    def __str__(self) -> str:
        return f"{self.nombre} ({self.tipo})"


class Equipamiento(models.Model):
    class Tipo(models.TextChoices):
        SOPORTE_VITAL = "soporte_vital", "Soporte Vital"
        APOYO_MONITORIZACION = "apoyo_monitorizacion", "Apoyo y Monitorización"

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.modelo} ({self.modelo}) | {self.item}"


class Quiebre(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=500)

    class Meta:
        unique_together = [("institucion", "medicamento")]
