import pytest
from datetime import date
from maestro.models import Item, Equipamiento, Institucion, Medicamento

# INSTITUCION
@pytest.mark.django_db
def test_add_institucion(client):

    data = {
        "nombre":"CLINICA DEL DCC",
        "tipo":"clinica",
        "titularidad":"privado",
        "num_camas_uti":2,
        "num_camas_uci":3,
        "factor":1.0,
    }

    response = client.post(
        "/maestro/instituciones",
        data,
        content_type="application/json",
    )
    assert response.status_code == 201, "endpoint no encontrado"
    assert response.data["nombre"] == data["nombre"]
    assert response.data["tipo"] == data["tipo"]
    assert response.data["titularidad"] == data["titularidad"]
    assert response.data["num_camas_uti"] == data["num_camas_uti"]
    assert response.data["num_camas_uci"] == data["num_camas_uci"]
    assert response.data["factor"] == data["factor"]

# MEDICAMENTO
@pytest.mark.django_db
def test_add_medicamento(client):

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

    response = client.post(
        "/maestro/medicamentos",
        data,
        content_type="application/json",
    )
    assert response.status_code == 201, "endpoint no encontrado"
    assert response.data["nombre_comercial"] == data["nombre_comercial"]
    assert response.data["nombre_generico"] == data["nombre_generico"]
    assert response.data["ingredientes"] == data["ingredientes"]
    assert response.data["concentracion"] == data["concentracion"]
    assert response.data["forma_presentacion"] == data["forma_presentacion"]
    assert response.data["via_administracion"] == data["via_administracion"]
    assert response.data["indicaciones_terapeuticas"] == data["indicaciones_terapeuticas"]
    assert response.data["contraindicaciones"] == data["contraindicaciones"]
    assert response.data["efectos_secundarios"] == data["efectos_secundarios"]
    assert response.data["instrucciones_dosificacion"] == data["instrucciones_dosificacion"]
    assert response.data["fabricante"] == data["fabricante"]
    assert response.data["informacion_almacenamiento"] == data["informacion_almacenamiento"]
    assert response.data["interacciones_medicamentosas"] == data["interacciones_medicamentosas"]



# ITEMS
@pytest.mark.django_db
def test_add_item(client):

    data = {
        "nombre":"Respirador mecanico test",
        "tipo":"soporte_vital",
    }

    response = client.post(
        "/maestro/items",
        data,
        content_type="application/json",
    )
    assert response.status_code == 201, "endpoint no encontrado"
    assert response.data["nombre"] == data["nombre"]
    assert response.data["tipo"] == data["tipo"]


# EQUIPAMIENTOS
@pytest.mark.django_db
def test_add_equipamiento(client):

    item_pk = 3

    data = {
        "marca":"toyota",
        "modelo":"soporte_vital",
        "item":item_pk,
    }

    response = client.post(
        "/maestro/equipamientos",
        data,
        content_type="application/json",
    )

    assert response.status_code == 201, "endpoint no encontrado"
    assert response.data["marca"] == data["marca"]
    assert response.data["modelo"] == data["modelo"]
    assert response.data["item"] == data["item"]


# QUIEBRE
@pytest.mark.django_db
def test_add_quiebre(client):

    data = {
        "nombre":"CLINICA DEL DCC 2",
        "tipo":"clinica",
        "titularidad":"privado",
        "num_camas_uti":2,
        "num_camas_uci":3,
        "factor": 1.0,
    }

    institucion = Institucion.objects.create(**data)
    medicamento = Medicamento.objects.filter(pk=1).first()

    data = {
        "institucion":institucion.id,
        "medicamento":medicamento.id,
        "cantidad":1000,
    }

    response = client.post(
        "/maestro/quiebres",
        data,
        content_type="application/json",
    )
    assert response.status_code == 201, "endpoint no encontrado"
    assert response.data["institucion"] == data["institucion"]
    assert response.data["medicamento"] == data["medicamento"]
    assert response.data["cantidad"] == data["cantidad"]
