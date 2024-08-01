import pytest
from datetime import date
from django.db.utils import IntegrityError
from maestro.models import Institucion, Medicamento, Quiebre


@pytest.mark.django_db
def test_lote_model():
    from stock.models import Lote

    medicamento = Medicamento.objects.all().first()
    fecha_vencimiento = date(2024, 7, 10)
    lote = Lote.objects.create(
        codigo="AU_PRMINC_100001_CL_CENABAST_20230710_20240816",
        medicamento=medicamento,
        cantidad=500,
        fecha_vencimiento=fecha_vencimiento,
    )

    assert lote.codigo == "AU_PRMINC_100001_CL_CENABAST_20230710_20240816"
    assert lote.medicamento == medicamento
    assert lote.cantidad == 500
    assert lote.fecha_vencimiento == fecha_vencimiento

    assert str(lote) == lote.codigo, "se debe usar el código como representación str del objeto"

    lote.medicamento.delete()
    assert Lote.objects.filter(id=lote.id).first() is None, "eliminar medicamento debe eliminar lote en cascada"


@pytest.mark.django_db
def test_consumo_model():
    from stock.models import Consumo

    institucion = Institucion.objects.all().first()
    medicamento = Medicamento.objects.all().first()
    fecha = date.today()

    consumo = Consumo.objects.create(
        institucion=institucion,
        medicamento=medicamento,
        cantidad=0,
    )

    assert consumo.institucion == institucion
    assert consumo.medicamento == medicamento
    assert consumo.cantidad == 0
    assert consumo.fecha is not None, "la fecha por defecto debe ser la del día en que se genera el consumo"
    assert consumo.fecha == fecha, "la fecha por defecto debe ser la del día en que se genera el consumo"

    consumo.cantidad = -5
    with pytest.raises(IntegrityError):
        consumo.save()

        consumo = Consumo.objects.get(id=consumo.id)
        assert consumo.cantidad >= 0, "consumo debe ser mayor o igual que cero"


@pytest.mark.django_db
def test_stock_model():
    from stock.models import Stock

    quiebre = Quiebre.objects.all().last()
    fecha = date.today()

    s = Stock.objects.create(
        institucion=quiebre.institucion,
        medicamento=quiebre.medicamento,
    )

    assert s.institucion == quiebre.institucion
    assert s.medicamento == quiebre.medicamento
    assert s.cantidad == 0, "el stock inicial siempre debe ser cero"
    assert s.has_quiebre is False, "el stock inicial no debe tener quiebre"
    assert s.fecha_actualizacion == fecha, "la fecha de actualizacion es siempre la actual"

    _, created = Stock.objects.get_or_create(
        institucion=quiebre.institucion,
        medicamento=quiebre.medicamento,
    )
    assert not created, "institucion y medicamento deben ser unique together"


@pytest.mark.django_db
def test_movimiento_model():
    from stock.models import Lote, Movimiento

    institucion = Institucion.objects.all().first()
    lote = Lote.objects.all().first()
    fecha = date.today()

    movimiento = Movimiento.objects.create(institucion=institucion, lote=lote)

    assert movimiento.institucion == institucion
    assert movimiento.lote == lote
    assert movimiento.fecha == fecha, "la fecha por defecto debe ser la del día en que se genera el movimiento"

    with pytest.raises(IntegrityError) as exc_info:
        Movimiento.objects.create(institucion=institucion, lote=lote)
    assert str(exc_info.value) == "UNIQUE constraint failed: stock_movimiento.lote_id", "un lote no puede estar en más de una institución"
