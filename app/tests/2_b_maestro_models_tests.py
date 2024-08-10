import pytest


@pytest.mark.django_db
def test_institucion_model():
    from maestro.models import Institucion

    data = {
        "nombre":"CLINICA DEL DCC",
        "tipo":"clinica",
        "titularidad":"privado",
        "num_camas_uti":2,
        "num_camas_uci":3,
        "factor":1.0,
    }


    institucion = Institucion.objects.create(**data)

    assert institucion.nombre == data["nombre"]
    assert institucion.tipo == data["tipo"]
    assert institucion.titularidad == data["titularidad"]
    assert institucion.num_camas_uti == data["num_camas_uti"]
    assert institucion.num_camas_uci == data["num_camas_uci"]

    assert str(institucion) == institucion.nombre, "se debe usar el nombre como representación str del objeto"


@pytest.mark.django_db
def test_medicamento_model():
    from maestro.models import Medicamento

    data = {
        "nombre_comercial" : "Ibupirac test",
        "nombre_generico" : "Ibuprofeno test",
        "ingredientes" : "Ibuprofeno test",
        "concentracion" : "400mg",
        "forma_presentacion" : "blister",
        "forma_farmaceutica" : "tabletas",
        "via_administracion" : "oral",
        "indicaciones_terapeuticas" : "Alivio temporal de dolores leves a moderados, como dolores de cabeza, dolores musculares, dolor de espalda, dolor de muelas, dolor menstrual y dolor de artritis.",
        "contraindicaciones" : "No utilizar en caso de alergia al ibuprofeno, úlcera péptica activa o hemorragia gastrointestinal, insuficiencia cardíaca grave o enfermedad hepática grave.",
        "efectos_secundarios" : "Algunos efectos secundarios pueden incluir malestar estomacal, náuseas, vómitos, diarrea, mareos, dolor de cabeza y erupciones en la piel. En casos raros, puede causar reacciones alérgicas graves.",
        "instrucciones_dosificacion" : "La dosis recomendada para adultos es de 400mg cada 4 a 6 horas, no excediendo los 1,200mg en 24 horas. Consulte a su médico para obtener instrucciones específicas.",
        "fabricante" : "Laboratorios Chile S.A.",
        "informacion_almacenamiento" : "Almacenar en un lugar fresco y seco, protegido de la luz y fuera del alcance de los niños.",
        "interacciones_medicamentosas" : "El ibuprofeno puede interactuar con otros medicamentos, como anticoagulantes, antihipertensivos, aspirina, corticosteroides y diuréticos. Consulte a su médico o farmacéutico para obtener información sobre posibles interacciones.",
    }


    medicamento = Medicamento.objects.create(**data)

    assert medicamento.nombre_comercial == data["nombre_comercial"]
    assert medicamento.nombre_generico == data["nombre_generico"]
    assert medicamento.ingredientes == data["ingredientes"]
    assert medicamento.concentracion == data["concentracion"]
    assert medicamento.forma_presentacion == data["forma_presentacion"]
    assert medicamento.forma_farmaceutica == data["forma_farmaceutica"]
    assert medicamento.via_administracion == data["via_administracion"]
    assert medicamento.indicaciones_terapeuticas == data["indicaciones_terapeuticas"]
    assert medicamento.contraindicaciones == data["contraindicaciones"]
    assert medicamento.efectos_secundarios == data["efectos_secundarios"]
    assert medicamento.instrucciones_dosificacion == data["instrucciones_dosificacion"]
    assert medicamento.fabricante == data["fabricante"]
    assert medicamento.informacion_almacenamiento == data["informacion_almacenamiento"]
    assert medicamento.interacciones_medicamentosas == data["interacciones_medicamentosas"]

    assert str(medicamento) == f"{medicamento.nombre_comercial} ({medicamento.nombre_generico}) | {medicamento.fabricante}", "se debe usar el nombre como representación str del objeto"


@pytest.mark.django_db
def test_item_model():
    from maestro.models import Item

    data = {
        "nombre":"Respirador mecanico test",
        "tipo":"soporte_vital",
    }


    item = Item.objects.create(**data)

    assert item.nombre == data["nombre"]
    assert item.tipo == data["tipo"]

    assert str(item) == f"{item.nombre} ({item.tipo})", "se debe usar el nombre tipo como representación str del objeto"


@pytest.mark.django_db
def test_equipamiento_model():
    from maestro.models import Equipamiento, Item

    item_pk = 3
    item = Item.objects.filter(pk=item_pk)

    data = {
        "marca":"toyota",
        "modelo":"soporte_vital",
        "item_id":item_pk,
    }


    equipamiento = Equipamiento.objects.create(**data)

    assert equipamiento.marca == data["marca"]
    assert equipamiento.modelo == data["modelo"]
    assert equipamiento.item_id == data["item_id"]

    assert str(equipamiento) == f"{equipamiento.modelo} ({equipamiento.modelo}) | {equipamiento.item}", "se debe usar el modelo modelo | item tipo como representación str del objeto"


@pytest.mark.django_db
def test_quiebre_model():
    from maestro.models import Institucion, Medicamento, Quiebre


    data = {
        "nombre":"CLINICA DEL DCC",
        "tipo":"clinica",
        "titularidad":"privado",
        "num_camas_uti":2,
        "num_camas_uci":3,
        "factor": 1.0,
    }

    institucion = Institucion.objects.create(**data)
    medicamento = Medicamento.objects.filter(pk=1).first()

    data_quiebre = {
        "institucion":institucion,
        "medicamento":medicamento,
        "cantidad":1000,
    }


    quiebre = Quiebre.objects.create(**data_quiebre)

    assert quiebre.institucion == data_quiebre["institucion"]
    assert quiebre.medicamento == data_quiebre["medicamento"]
    assert quiebre.cantidad == data_quiebre["cantidad"]