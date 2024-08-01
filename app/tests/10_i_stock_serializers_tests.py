import pytest
import json
from datetime import date
from maestro.models import Institucion, Medicamento
from stock.models import Lote, Consumo, Stock, Movimiento


@pytest.mark.django_db
def test_lote_serializer():
    from stock.serializers import LoteSerializer

    lote = Lote.objects.create(
        codigo="AU_PRMINC_100001_CL_CENABAST_20230710_20240816",
        medicamento=Medicamento.objects.all().first(),
        cantidad=50000,
        fecha_vencimiento=str(date(date.today().year + 1, 12, 31)),
    )
    data = {
        "id": lote.id,
        "codigo": lote.codigo,
        "medicamento": lote.medicamento.id,
        "cantidad": lote.cantidad,
        "fecha_vencimiento": lote.fecha_vencimiento,
    }

    serialized_data = LoteSerializer(data=data)
    serialized_object = LoteSerializer(lote)
    serialized_data.is_valid()

    assert json.dumps(serialized_object.data) == json.dumps(data), "data serializada no tiene el orden correcto"
    assert serialized_data.errors == {}, f"Errores: {serialized_data.errors}"


@pytest.mark.django_db
def test_consumo_serializer():
    from stock.serializers import ConsumoSerializer

    consumo = Consumo.objects.create(
        institucion=Institucion.objects.all().first(), medicamento=Medicamento.objects.all().first(), cantidad=0, fecha=str(date.today())
    )
    data = {
        "id": consumo.id,
        "institucion": consumo.institucion.id,
        "medicamento": consumo.medicamento.id,
        "cantidad": consumo.cantidad,
        "fecha": str(consumo.fecha),
    }

    serialized_data = ConsumoSerializer(data=data)
    serialized_object = ConsumoSerializer(consumo)
    serialized_data.is_valid()
    assert json.dumps(serialized_object.data) == json.dumps(data), "data serializada no tiene el orden correcto"
    assert serialized_data.errors == {}, f"Errores: {serialized_data.errors}"


@pytest.mark.django_db
def test_stock_serializer():
    from stock.serializers import StockSerializer

    stock = Stock.objects.create(
        institucion=Institucion.objects.all().first(),
        medicamento=Medicamento.objects.all().first(),
    )
    data = {
        "id": stock.id,
        "institucion": stock.institucion.id,
        "medicamento": stock.medicamento.id,
        "cantidad": stock.cantidad,
        "has_quiebre": stock.has_quiebre,
        "fecha_actualizacion": str(stock.fecha_actualizacion),
    }

    serialized_data = StockSerializer(data=data)
    serialized_object = StockSerializer(stock)
    serialized_data.is_valid()
    assert json.dumps(serialized_object.data) == json.dumps(data), "data serializada no tiene el orden correcto"
    assert serialized_data.errors == {}, f"Errores: {serialized_data.errors}"


@pytest.mark.django_db
def test_movimiento_serializer():
    from stock.serializers import MovimientoSerializer

    movimiento = Movimiento.objects.create(
        institucion=Institucion.objects.all().first(),
        lote=Lote.objects.all().first(),
        fecha=date.today(),
    )
    data = {
        "id": movimiento.id,
        "institucion": movimiento.institucion.id,
        "lote": movimiento.lote.id,
        "fecha": str(movimiento.fecha),
    }

    serialized_data = MovimientoSerializer(data=data)
    serialized_object = MovimientoSerializer(movimiento)
    serialized_data.is_valid()
    assert json.dumps(serialized_object.data) == json.dumps(data), "data serializada no tiene el orden correcto"
    assert (
        str(serialized_data.errors["lote"]) == "[ErrorDetail(string='Ya existe movimiento con este lote.', code='unique')]"
    ), f"Errores: {serialized_data.errors}"
