import pytest
from datetime import date


@pytest.mark.django_db
def test_consumo_medicamento(client):
    response = client.get("/stock/consumos-medicamento", content_type="application/json")
    assert response.status_code == 200, "endpoint no encontrado"
    assert len(response.data) == 1, "se obtuvieron más resultados de los esperados"

    data = {5: {"medicamento": 5, "cantidad": 499500, "consumos": [{"institucion": 1, "cantidad": 499500, "fecha": date(2023, 7, 28)}]}}
    assert response.data == data, f"data no tiene los datos esperados ({data})"


@pytest.mark.django_db
def test_consumo_medicamento_id(client):
    response = client.get("/stock/consumos-medicamento/10", content_type="application/json")
    assert response.status_code == 200, "endpoint no encontrado"
    assert len(response.data) == 0, "se obtuvieron más resultados de los esperados"

    response = client.get("/stock/consumos-medicamento/5", content_type="application/json")
    assert response.status_code == 200, "endpoint no encontrado"
    assert len(response.data) == 1, "se obtuvieron más resultados de los esperados"


@pytest.mark.django_db
def test_movimientos_medicamento(client):
    response = client.get("/stock/movimientos-medicamento", content_type="application/json")
    assert response.status_code == 200, "endpoint no encontrado"
    assert len(response.data) == 1, "se obtuvieron más resultados de los esperados"

    data = {"medicamento": 5, "movimientos": [{"lote": 20, "institucion": 1, "fecha": date(2023, 7, 28)}]}
    assert list(response.data)[0] == data, f"data no tiene los datos esperados ({data})"


@pytest.mark.django_db
def test_movimientos_medicamento_id(client):
    response = client.get("/stock/movimientos-medicamento/10", content_type="application/json")
    assert response.status_code == 200, "endpoint no encontrado"
    assert len(response.data) == 0, "se obtuvieron más resultados de los esperados"

    response = client.get("/stock/movimientos-medicamento/5", content_type="application/json")
    assert response.status_code == 200, "endpoint no encontrado"
    assert len(response.data) == 1, "se obtuvieron más resultados de los esperados"


@pytest.mark.django_db
def test_disponibilidad_medicamento(client):
    response = client.get("/stock/disponibilidad-medicamento", content_type="application/json")
    assert response.status_code == 200, "endpoint no encontrado"
    assert len(response.data) == 1, "se obtuvieron más resultados de los esperados"

    data = {5: {"medicamento": 5, "cantidad": 500, "stocks": [{"institucion": 1, "cantidad": 500}]}}
    assert response.data == data, f"data no tiene los datos esperados ({data})"


@pytest.mark.django_db
def test_disponibilidad_medicamento_id(client):
    response = client.get("/stock/disponibilidad-medicamento/10", content_type="application/json")
    assert response.status_code == 200, "endpoint no encontrado"
    assert len(response.data) == 0, "se obtuvieron más resultados de los esperados"

    response = client.get("/stock/disponibilidad-medicamento/5", content_type="application/json")
    assert response.status_code == 200, "endpoint no encontrado"
    assert len(response.data) == 1, "se obtuvieron más resultados de los esperados"


@pytest.mark.django_db
def test_quiebre_stock(client):
    response = client.get("/stock/quiebre-stock", content_type="application/json")
    assert response.status_code == 200, "endpoint no encontrado"
    assert len(response.data) == 1, "se obtuvieron más resultados de los esperados"

    data = [{"institucion": 1, "medicamento": 5, "stock": 500, "quiebre": 500}]
    assert response.data == data, f"data no tiene los datos esperados ({data})"


@pytest.mark.django_db
def test_alerta_caducidad_lote(client):
    response = client.get("/stock/alerta-caducidad-lote", content_type="application/json")
    assert response.status_code == 200, "endpoint no encontrado"
    assert len(response.data) == 3, "se obtuvieron más resultados de los esperados"

    data = [
        {
            "id": 16,
            "codigo": "SA_NAHRD_5j2mDrL9x0xKCl_20230721_20330721",
            "medicamento": 23,
            "cantidad": 450000,
            "fecha_vencimiento": "2022-07-21",
        },
        {
            "id": 17,
            "codigo": "SE_ASBRD_8N9uLf3P8qfNCl_20230730_20330730",
            "medicamento": 34,
            "cantidad": 775000,
            "fecha_vencimiento": "2022-07-30",
        },
        {
            "id": 18,
            "codigo": "TR_ABDRG_5p3WLiH4m7eFCl_20230726_20330726",
            "medicamento": 2,
            "cantidad": 575000,
            "fecha_vencimiento": "2022-07-26",
        },
    ]
    assert response.data == data, f"data no tiene los datos esperados ({data})"
