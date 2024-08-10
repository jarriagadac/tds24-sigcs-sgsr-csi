import pytest
import json
from maestro.models import Item, Equipamiento, Institucion, Medicamento, Quiebre


@pytest.mark.django_db
def test_institucion_serializer():
    from maestro.serializers import InstitucionSerializer

    institucion = Institucion.objects.create(
        nombre = "INSTITUCIÓN TEST",
        tipo = "farmacia",
        titularidad = "publico",
        num_camas_uti = 0,
        num_camas_uci = 0,
        factor = 0.0
    )
    
    data = {
        "nombre": institucion.nombre,
        "tipo" :institucion.tipo,
        "titularidad" : institucion.titularidad,
        "num_camas_uti" : institucion.num_camas_uti,
        "num_camas_uci" : institucion.num_camas_uci,
        "factor" : institucion.factor
    }

    serialized_data = InstitucionSerializer(data=data)
    serializer_item = InstitucionSerializer(institucion)
    serialized_data.is_valid()
    assert json.dumps(serializer_item.data) == json.dumps(data), "data serializada no tiene el mismo orden"
    assert serialized_data.errors == {}, f"Errores: {serialized_data.errors}"


@pytest.mark.django_db
def test_medicamento_serializer():
    from maestro.serializers import MedicamentoSerializer

    medicamento = Medicamento.objects.create(
        nombre_comercial = "medicamento prueba",
        nombre_generico = "Mprueba",
        ingredientes = "test",
        concentracion = "400mg",
        forma_presentacion = "blister",
        forma_farmaceutica = "tabletas",
        via_administracion = "oral",
        indicaciones_terapeuticas = "Alivio temporal de dolores leves a moderados, como dolores de cabeza, dolores musculares, dolor de espalda, dolor de muelas, dolor menstrual y dolor de artritis.",
        contraindicaciones = "No utilizar en caso de alergia al ibuprofeno, úlcera péptica activa o hemorragia gastrointestinal, insuficiencia cardíaca grave o enfermedad hepática grave.",
        efectos_secundarios = "Algunos efectos secundarios pueden incluir malestar estomacal, náuseas, vómitos, diarrea, mareos, dolor de cabeza y erupciones en la piel. En casos raros, puede causar reacciones alérgicas graves.",
        instrucciones_dosificacion = "La dosis recomendada para adultos es de 400mg cada 4 a 6 horas, no excediendo los 1,200mg en 24 horas. Consulte a su médico para obtener instrucciones específicas.",
        fabricante = "Laboratorios Chile S.A.",
        informacion_almacenamiento = "Almacenar en un lugar fresco y seco, protegido de la luz y fuera del alcance de los niños.",
        interacciones_medicamentosas = "El ibuprofeno puede interactuar con otros medicamentos, como anticoagulantes, antihipertensivos, aspirina, corticosteroides y diuréticos. Consulte a su médico o farmacéutico para obtener información sobre posibles interacciones."
    )
    
    data = {
        "nombre_comercial": medicamento.nombre_comercial,
        "nombre_generico": medicamento.nombre_generico,
        "ingredientes": medicamento.ingredientes,
        "concentracion": medicamento.concentracion,
        "forma_presentacion": medicamento.forma_presentacion,
        "forma_farmaceutica": medicamento.forma_farmaceutica,
        "via_administracion": medicamento.via_administracion,
        "indicaciones_terapeuticas": medicamento.indicaciones_terapeuticas,
        "contraindicaciones": medicamento.contraindicaciones,
        "efectos_secundarios": medicamento.efectos_secundarios,
        "instrucciones_dosificacion": medicamento.instrucciones_dosificacion,
        "fabricante": medicamento.fabricante,
        "informacion_almacenamiento": medicamento.informacion_almacenamiento,
        "interacciones_medicamentosas": medicamento.interacciones_medicamentosas
    }

    serialized_data = MedicamentoSerializer(data=data)
    serializer_item = MedicamentoSerializer(medicamento)
    serialized_data.is_valid()
    assert json.dumps(serializer_item.data) == json.dumps(data), "data serializada no tiene el mismo orden"
    assert serialized_data.errors == {}, f"Errores: {serialized_data.errors}"

@pytest.mark.django_db
def test_item_serializer():
    from maestro.serializers import ItemSerializer

    item = Item.objects.create(
        nombre="Respirador Mecánico prueba",
        tipo="soporte_vital",
    )

    data = {
        "nombre": item.nombre,
        "tipo": item.tipo,
    }

    serialized_data = ItemSerializer(data=data)
    serializer_item = ItemSerializer(item)
    serialized_data.is_valid()
    assert json.dumps(serializer_item.data) == json.dumps(data), "data serializada no tiene el mismo orden"
    assert serialized_data.errors == {}, f"Errores: {serialized_data.errors}"

@pytest.mark.django_db
def test_equipamiento_serializer():
    from maestro.serializers import EquipamientoSerializer

    item = Item.objects.create(
        nombre="Respirador Mecánico prueba",
        tipo="soporte_vital",
    )

    equipamiento = Equipamiento.objects.create(
        item=item,
        marca="GE Healthcare prueba",
        modelo="Dash 5000 prueba",
    )

    data = {"item": equipamiento.item.id, "marca": equipamiento.marca, "modelo": equipamiento.modelo}

    serialized_data = EquipamientoSerializer(data=data)
    serializer_item = EquipamientoSerializer(equipamiento)
    serialized_data.is_valid()
    assert json.dumps(serializer_item.data) == json.dumps(data), "data serializada no tiene el mismo orden"
    assert serialized_data.errors == {}, f"Errores: {serialized_data.errors}"

@pytest.mark.django_db
def test_quiebre_serializer():
    from maestro.serializers import QuiebreSerializer

    quiebre_existente = Quiebre.objects.all().first()

    if quiebre_existente is None:
        raise Exception("Quiebre existente sin datos")

    data = {
        "institucion": quiebre_existente.institucion.id,
        "medicamento": quiebre_existente.medicamento.id,
        "cantidad": quiebre_existente.cantidad
    }

    serializer_item = QuiebreSerializer(quiebre_existente)

    serialized_data = QuiebreSerializer(data=data)

    assert not serialized_data.is_valid(), f"Errores: {serialized_data.errors}"

    assert serializer_item.data == data, (
        f"Data serializada no coincide: "
        f"expected {data} but got {serializer_item.data}"
    )

