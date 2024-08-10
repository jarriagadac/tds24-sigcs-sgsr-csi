import pytest
import json
from maestro.models import Medicamento, Institucion, Item, Equipamiento, Quiebre


@pytest.mark.django_db
def test_institucion_serializer():
    from maestro.serializers import InstitucionSerializer

    institucion = Institucion.objects.create(
        nombre="Institucion de prueba",
        tipo=Institucion.Tipo.BODEGA,
        titularidad=Institucion.Titularidad.PRIVADO,
        num_camas_uti=2,
        num_camas_uci=2,
        factor=1.0,
    )
    data = {
        "nombre": "Institucion de prueba",
        "tipo": Institucion.Tipo.BODEGA,
        "titularidad": Institucion.Titularidad.PRIVADO,
        "num_camas_uti": 2,
        "num_camas_uci": 2,
    }
    serialized_data = InstitucionSerializer(data=data)
    serialized_object = InstitucionSerializer(institucion)
    serialized_data.is_valid()
    assert json.dumps(serialized_object.data) == json.dumps(data), "data serializada no tiene el orden correcto"
    assert serialized_data.errors == {}, f"Errores: {serialized_data.errors}"


@pytest.mark.django_db
def test_medicamento_serializer():
    from maestro.serializers import MedicamentoSerializer

    medicamento = Medicamento.objects.create(
        nombre_comercial="Penicilina",
        nombre_generico="Penicilina",
        ingredientes="Penicilina",
        concentracion="500mg",
        forma_presentacion=Medicamento.FormaPresentacion.FRASCO,
        forma_farmaceutica=Medicamento.FormaFarmaceutica.TABLETAS,
        via_administracion=Medicamento.Via.ORAL,
        indicaciones_terapeuticas="Tratamiento de infecciones bacterianas",
        contraindicaciones="Alergia a la penicilina o a otros antibióticos betalactámicos",
        efectos_secundarios="Náuseas, vómitos, diarrea, reacciones alérgicas",
        instrucciones_dosificacion="Adultos: 250-500 mg cada 6-8 horas por vía oral",
        fabricante="Laboratorios ABC",
        informacion_almacenamiento="Conservar a temperatura ambiente, en un lugar seco y fuera del alcance de los niños",
        interacciones_medicamentosas="Puede interactuar con anticoagulantes y algunos diuréticos",
    )
    data = {
        "nombre_comercial": "Penicilina",
        "nombre_generico": "Penicilina",
        "ingredientes": "Penicilina",
        "concentracion": "500mg",
        "forma_presentacion": Medicamento.FormaPresentacion.FRASCO,
        "forma_farmaceutica": Medicamento.FormaFarmaceutica.TABLETAS,
        "via_administracion": Medicamento.Via.ORAL,
        "indicaciones_terapeuticas": "Tratamiento de infecciones bacterianas",
        "contraindicaciones": "Alergia a la penicilina o a otros antibióticos betalactámicos",
        "efectos_secundarios": "Náuseas, vómitos, diarrea, reacciones alérgicas",
        "instrucciones_dosificacion": "Adultos: 250-500 mg cada 6-8 horas por vía oral",
        "fabricante": "Laboratorios ABC",
        "informacion_almacenamiento": "Conservar a temperatura ambiente, en un lugar seco y fuera del alcance de los niños",
        "interacciones_medicamentosas": "Puede interactuar con anticoagulantes y algunos diuréticos",
    }
    serialized_data = MedicamentoSerializer(data=data)
    serialized_object = MedicamentoSerializer(medicamento)
    serialized_data.is_valid()
    assert json.dumps(serialized_object.data) == json.dumps(data), "data serializada no tiene el orden correcto"
    assert serialized_data.errors == {}, f"Errores: {serialized_data.errors}"


@pytest.mark.django_db
def test_item_serializer():
    from maestro.serializers import ItemSerializer

    item = Item.objects.create(nombre="Equipo de Monitorización Neurológica", tipo=Item.Tipo.APOYO_MONITORIZACION)
    data = {"nombre": "Equipo de Monitorización Neurológica", "tipo": Item.Tipo.APOYO_MONITORIZACION}
    serialized_object = ItemSerializer(item)
    serialized_data = ItemSerializer(data=data)
    serialized_data.is_valid()
    assert json.dumps(serialized_object.data) == json.dumps(data), "data serializada no tiene el orden correcto"
    assert serialized_data.errors == {}, f"Errores: {serialized_data.errors}"


@pytest.mark.django_db
def test_equipamiento_serializer():
    from maestro.serializers import EquipamientoSerializer

    item = Item.objects.all().first()
    equipamiento = Equipamiento.objects.create(item=item, marca="Medtronic", modelo="Puritan Bennet 840")
    data = {"item": equipamiento.item.id, "marca": "Medtronic", "modelo": "Puritan Bennet 840"}
    serialized_object = EquipamientoSerializer(equipamiento)
    serialized_data = EquipamientoSerializer(data=data)
    serialized_data.is_valid()
    assert json.dumps(serialized_object.data) == json.dumps(data), "data serializada no tiene el orden correcto"
    assert serialized_data.errors == {}, f"Errores: {serialized_data.errors}"


@pytest.mark.django_db
def test_quiebre_serializer():
    from maestro.serializers import QuiebreSerializer

    medicamento = Medicamento.objects.all().first()
    institucion = Institucion.objects.all().first()
    quiebre = Quiebre.objects.create(medicamento=medicamento, institucion=institucion, cantidad=1)
    data = {"medicamento": quiebre.medicamento.id, "institucion": quiebre.institucion.id, "cantidad": 1}
    serialized_object = QuiebreSerializer(quiebre)
    serialized_data = QuiebreSerializer(data=data)
    serialized_data.is_valid()
    assert json.dumps(serialized_object.data) == json.dumps(data), "data serializada no tiene el orden correcto"
    assert serialized_data.errors == {}, f"Errores: {serialized_data.errors}"
