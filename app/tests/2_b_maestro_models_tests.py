import pytest
from django.core.exceptions import ValidationError


@pytest.mark.django_db
def test_institucion_model():
    from maestro.models import Institucion

    institucion = Institucion.objects.create(
        nombre="Institucion de prueba",
        tipo=Institucion.Tipo.BODEGA,
        titularidad=Institucion.Titularidad.PRIVADO,
        num_camas_uti=2,
        num_camas_uci=2,
        factor=1.0,
    )

    assert str(institucion) == "Institucion de prueba"
    assert institucion.tipo == Institucion.Tipo.BODEGA
    assert institucion.titularidad == Institucion.Titularidad.PRIVADO
    assert institucion.num_camas_uci == 2
    assert institucion.num_camas_uti == 2
    assert institucion.factor == 1.0

    # Revisar si campo 'Titularidad' no pertenece a las opciones establecidas
    institucion.titularidad = "Titularidad no permitida"
    with pytest.raises(ValidationError):
        institucion.full_clean()
    institucion.titularidad = Institucion.Titularidad.PRIVADO

    # Revisar si campo 'Tipo' no pertenece a las opciones establecidas
    institucion.tipo = "Tipo no permitido"
    with pytest.raises(ValidationError):
        institucion.full_clean()
    institucion.tipo = Institucion.Tipo.BODEGA

    # Revisar si campo 'num_camas_uci' es mayor o igual a 0
    institucion.num_camas_uci = -1
    with pytest.raises(ValidationError):
        institucion.full_clean()
    institucion.num_camas_uci = 1

    # Revisar si campo 'num_camas_uti' es mayor o igual a 0
    institucion.num_camas_uti = -5
    with pytest.raises(ValidationError):
        institucion.full_clean()
    institucion.num_camas_uti = 1

    # Revisar si campo 'factor' es de tipo 'float'
    institucion.factor = "Valor string, no float"
    with pytest.raises(ValidationError):
        institucion.full_clean()


@pytest.mark.django_db
def test_medicamento_model():
    from maestro.models import Medicamento

    medicamento = Medicamento.objects.create(
        nombre_comercial="Penicilina",
        ingredientes="Penicilina",
        concentracion="500mg",
        forma_presentacion=Medicamento.FormaPresentacion.FRASCO,
        forma_farmaceutica=Medicamento.FormaFarmaceutica.TABLETAS,
        via_administracion=Medicamento.Via.ORAL,
        indicaciones_terapeuticas="Tratamiento de infecciones bacterianas",
        fabricante="Laboratorios ABC",
        interacciones_medicamentosas="Puede interactuar con anticoagulantes y algunos diuréticos",
    )

    assert medicamento.nombre_comercial == "Penicilina"
    assert medicamento.nombre_generico is None, "Nombre generico por defecto debe ser 'blank'"
    assert medicamento.contraindicaciones is None, "Contraindicaciones por defecto debe ser 'blank'"
    assert medicamento.efectos_secundarios is None, "Efectos Secundarios por defecto debe ser 'blank'"
    assert medicamento.informacion_almacenamiento is None, "Información Almacenamiento por defecto debe ser 'blank'"
    assert medicamento.instrucciones_dosificacion is None
    assert medicamento.fabricante == "Laboratorios ABC"
    assert medicamento.interacciones_medicamentosas == "Puede interactuar con anticoagulantes y algunos diuréticos"

    medicamento.nombre_generico = "Penicilina"
    assert str(medicamento) == "Penicilina (Penicilina) | Laboratorios ABC"

    # Revisar el largo del campo 'nombre_comercial'
    medicamento.nombre_comercial = "A" * 256
    with pytest.raises(ValidationError):
        medicamento.full_clean()
    medicamento.nombre_comercial = "Penicilina"

    # Revisar el largo del campo 'nombre_generico'
    medicamento.nombre_generico = "B" * 256
    with pytest.raises(ValidationError):
        medicamento.full_clean()
    medicamento.nombre_generico = "Penicilina"

    # Revisar el largo del campo 'ingredientes'
    medicamento.ingredientes = "C" * 256
    with pytest.raises(ValidationError):
        medicamento.full_clean()
    medicamento.ingredientes = "Penicilina"

    # Revisar el largo del campo 'concentracion'
    medicamento.concentracion = "D" * 256
    with pytest.raises(ValidationError):
        medicamento.full_clean()
    medicamento.concentracion = "500mg"

    # Revisar valores no válidos para campos con opciones definidas
    medicamento.forma_presentacion = "Invalid Forma Presentacion"
    with pytest.raises(ValidationError):
        medicamento.full_clean()
    medicamento.forma_presentacion = Medicamento.FormaPresentacion.FRASCO

    medicamento.forma_farmaceutica = "Invalid Forma Farmaceutica"
    with pytest.raises(ValidationError):
        medicamento.full_clean()
    medicamento.forma_farmaceutica = Medicamento.FormaFarmaceutica.TABLETAS

    medicamento.via_administracion = "Invalid Via Administración"
    with pytest.raises(ValidationError):
        medicamento.full_clean()
    medicamento.via_administracion = Medicamento.Via.ORAL

    # Revisar el largo del campo 'indicaciones_terapeuticas'
    medicamento.indicaciones_terapeuticas = "E" * 256
    with pytest.raises(ValidationError):
        medicamento.full_clean()
    medicamento.indicaciones_terapeuticas = "Tratamiento de infecciones bacterianas"

    # Revisar el largo del campo 'contraindicaciones'
    medicamento.contraindicaciones = "E" * 256
    with pytest.raises(ValidationError):
        medicamento.full_clean()
    medicamento.contraindicaciones = "Alergia a la penicilina"

    # Revisar el largo del campo 'efectos_secundarios'
    medicamento.efectos_secundarios = "E" * 256
    with pytest.raises(ValidationError):
        medicamento.full_clean()
    medicamento.efectos_secundarios = "Nauseas, erupciones cutáneas"

    # Revisar el largo del campo 'instrucciones_dosificacion'
    medicamento.instrucciones_dosificacion = "E" * 256
    with pytest.raises(ValidationError):
        medicamento.full_clean()
    medicamento.instrucciones_dosificacion = "1 tableta cada 8 horas"

    # Revisar el largo del campo 'fabricante'
    medicamento.fabricante = "E" * 256
    with pytest.raises(ValidationError):
        medicamento.full_clean()
    medicamento.fabricante = "Laboratorios ABC"

    # Revisar el largo del campo 'informacion_almacenamiento'
    medicamento.informacion_almacenamiento = "E" * 256
    with pytest.raises(ValidationError):
        medicamento.full_clean()
    medicamento.informacion_almacenamiento = "Conservar en lugar seco y fresco"

    # Revisar el largo del campo 'interacciones_medicamentosas'
    medicamento.interacciones_medicamentosas = "E" * 256
    with pytest.raises(ValidationError):
        medicamento.full_clean()
    medicamento.interacciones_medicamentosas = "Puede interactuar con anticoagulantes y algunos diuréticos"


@pytest.mark.django_db
def test_item_model():
    from maestro.models import Item

    item = Item.objects.create(nombre="Monitor de Signos Vitales", tipo=Item.Tipo.SOPORTE_VITAL)
    assert item.nombre == "Monitor de Signos Vitales"
    assert item.tipo == Item.Tipo.SOPORTE_VITAL
    assert str(item) == "Monitor de Signos Vitales (soporte_vital)"

    # Revisar el largo del campo 'nombre'
    item.nombre = "A" * 256
    with pytest.raises(ValidationError):
        item.full_clean()
    item.nombre = "Puede interactuar con anticoagulantes y algunos diuréticos"

    item.tipo = "Invalid Tipo"
    with pytest.raises(ValidationError):
        item.full_clean()


@pytest.mark.django_db
def test_equipamiento_model():
    from maestro.models import Equipamiento, Item

    item = Item.objects.all().first()
    equipamiento = Equipamiento.objects.create(item=item, marca="Respirador Mecánico", modelo="Modelo")
    assert equipamiento.item == item
    assert equipamiento.marca == "Respirador Mecánico"
    assert equipamiento.modelo == "Modelo"
    assert str(equipamiento) == "Modelo (Modelo) | Respirador Mecánico (soporte_vital)"

    # Revisar el largo del campo 'marca'
    equipamiento.marca = "A" * 257
    with pytest.raises(ValidationError):
        equipamiento.full_clean()
    equipamiento.marca = "Respirador Mecánico"

    # Revisar el largo del campo 'modelo'
    equipamiento.modelo = "A" * 257
    with pytest.raises(ValidationError):
        equipamiento.full_clean()
    equipamiento.modelo = "Modelo"

    equipamiento.item.delete()
    assert Equipamiento.objects.filter(id=equipamiento.id).first() is None, "Eliminar item debería eliminar Equipamiento"


@pytest.mark.django_db
def test_quiebre_model():
    from maestro.models import Quiebre, Institucion, Medicamento

    institucion = Institucion.objects.all().first()
    medicamento = Medicamento.objects.all().first()
    quiebre = Quiebre.objects.create(institucion=institucion, medicamento=medicamento)
    assert quiebre.institucion == institucion
    assert quiebre.medicamento == medicamento
    assert quiebre.cantidad == 500, "Cantidad por defecto, debe ser 500"

    _, created = Quiebre.objects.get_or_create(institucion=quiebre.institucion, medicamento=quiebre.medicamento)

    assert not created, "LLaves foraneas 'institucion' y 'medicamento' son 'unique_together"
