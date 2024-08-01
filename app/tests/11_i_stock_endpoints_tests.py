import pytest
from datetime import date


# MOVIMIENTOS
@pytest.mark.django_db
def test_add_movimientos(client):
    response = client.post(
        "/stock/movimientos",
        {
            "institucion": 1,
            "lote": 1,
        },
        content_type="application/json",
    )
    assert response.status_code == 201, "endpoint no encontrado"
    assert response.data["institucion"] == 1
    assert response.data["lote"] == 1
    assert response.data["fecha"] == str(date.today())


@pytest.mark.django_db
def test_list_movimientos(client):
    client.post(
        "/stock/movimientos",
        {
            "institucion": 1,
            "lote": 1,
        },
        content_type="application/json",
    )
    response = client.get("/stock/movimientos", content_type="application/json")
    assert response.status_code == 200, "endpoint no encontrado"
    assert len(response.data) == 2, "se agregó más de un movimiento en la base de datos"


@pytest.mark.django_db
def test_get_movimientos(client):
    client.post(
        "/stock/movimientos",
        {
            "institucion": 1,
            "lote": 1,
        },
        content_type="application/json",
    )
    response = client.get("/stock/movimientos/1", content_type="application/json")
    assert response.status_code == 200, "endpoint no encontrado"
    assert response.data["id"] == 1, "no se obtuvieron movimientos"


@pytest.mark.django_db
def test_delete_movimientos(client):
    client.post(
        "/stock/movimientos",
        {
            "institucion": 1,
            "lote": 1,
        },
        content_type="application/json",
    )
    response = client.delete("/stock/movimientos/1", content_type="application/json")
    assert response.status_code == 204, "endpoint no encontrado"

    response = client.get("/stock/movimientos/1", content_type="application/json")
    assert response.status_code == 404, "el movimiento no fue eliminado"


@pytest.mark.django_db
def test_add_movimiento_invalid_json(client):
    response = client.post(
        "/stock/movimientos",
        {
            "id_institucion": 1,
            "id_lote": 1,
        },
        content_type="application/json",
    )
    assert response.status_code == 400, "endpoint no encontrado / no se debe permitir data mal formada"


# CONSUMOS
@pytest.mark.django_db
def test_add_consumo(client):
    response = client.post(
        "/stock/consumos",
        {
            "institucion": 1,
            "medicamento": 26,
            "cantidad": 0,
        },
        content_type="application/json",
    )
    assert response.status_code == 201, "endpoint no encontrado"
    assert response.data["institucion"] == 1
    assert response.data["cantidad"] == 0
    assert response.data["medicamento"] == 26
    assert response.data["fecha"] == str(date.today())


@pytest.mark.django_db
def test_list_consumo(client):
    client.post(
        "/stock/consumos",
        {
            "institucion": 1,
            "medicamento": 26,
            "cantidad": 0,
        },
        content_type="application/json",
    )
    response = client.get("/stock/consumos", content_type="application/json")
    assert response.status_code == 200, "endpoint no encontrado"
    assert len(response.data) == 2, "se agregó más de un consumo en la base de datos"


@pytest.mark.django_db
def test_get_consumo(client):
    client.post(
        "/stock/consumos",
        {
            "institucion": 1,
            "medicamento": 26,
            "cantidad": 0,
        },
        content_type="application/json",
    )
    response = client.get("/stock/consumos/1", content_type="application/json")
    assert response.status_code == 200, "endpoint no encontrado"
    assert response.data["id"] == 1, "no se obtuvieron consumos"


@pytest.mark.django_db
def test_delete_consumo(client):
    client.post(
        "/stock/consumos",
        {
            "institucion": 1,
            "medicamento": 26,
            "cantidad": 0,
        },
        content_type="application/json",
    )
    response = client.delete("/stock/consumos/1", content_type="application/json")
    assert response.status_code == 204, "endpoint no encontrado"

    response = client.get("/stock/consumos/1", content_type="application/json")
    assert response.status_code == 404, "el movimiento no fue eliminado"


@pytest.mark.django_db
def test_add_consumo_invalid_json(client):
    response = client.post(
        "/stock/consumos",
        {
            "id_institucion": 1,
            "id_medicamento": 26,
            "cantidad": 0,
        },
        content_type="application/json",
    )
    assert response.status_code == 400, "endpoint no encontrado / no se debe permitir data mal formada"
