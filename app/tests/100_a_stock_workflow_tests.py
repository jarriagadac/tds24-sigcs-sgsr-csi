import pytest
from datetime import date


@pytest.mark.django_db
def test_workflow_calculo_stock():
    from maestro.models import Institucion, Medicamento
    from stock.models import Lote, Consumo, Stock, Movimiento
    from .functions import upd_stock_medicamento_institucion

    institucion = Institucion.objects.all().first()
    medicamento = Medicamento.objects.all().first()
    # creo/actualizo los stock por medicamento e institucion
    # esta función inicializa los stock de medicamento / institución
    upd_stock_medicamento_institucion()

    stock = Stock.objects.filter(institucion=institucion, medicamento=medicamento).first()
    assert callable(getattr(stock, "upd_cantidad", None)), "método upd_cantidad no encontrado en modelo de Stock"

    fecha_vencimiento = date(date.today().year + 1, date.today().month, date.today().day)
    lote1 = Lote.objects.create(codigo="LOTE_TEST_1", medicamento=medicamento, cantidad=5000, fecha_vencimiento=fecha_vencimiento)
    lote2 = Lote.objects.create(codigo="LOTE_TEST_2", medicamento=medicamento, cantidad=10000, fecha_vencimiento=fecha_vencimiento)
    # lote4 = Lote.objects.create(codigo="LOTE_TEST_4", medicamento=medicamento, cantidad=1500, fecha_vencimiento=date.today())
    Movimiento.objects.create(institucion=institucion, lote=lote1)
    Movimiento.objects.create(institucion=institucion, lote=lote2)
    stock = Stock.objects.filter(institucion=institucion, medicamento=medicamento).first()
    assert stock.cantidad == 15000, "cada movimiento debe actualizar (aumentar) la cantidad del stock"

    Consumo.objects.create(institucion=institucion, medicamento=medicamento, cantidad=10000)
    stock = Stock.objects.filter(institucion=institucion, medicamento=medicamento).first()
    assert stock.cantidad == 5000, "cada consumo debe actualizar (descontar) la cantidad del stock"


@pytest.mark.django_db
def test_workflow_calculo_quiebre_stock():
    from maestro.models import Quiebre
    from stock.models import Lote, Consumo, Stock, Movimiento
    from .functions import upd_stock_medicamento_institucion

    quiebre = Quiebre.objects.all().first()
    institucion = quiebre.institucion
    medicamento = quiebre.medicamento
    upd_stock_medicamento_institucion()

    stock = Stock.objects.filter(institucion=institucion, medicamento=medicamento).first()
    assert callable(getattr(stock, "upd_has_quiebre", None)), "método upd_has_quiebre no encontrado en modelo de Stock"

    fecha_vencimiento = date(date.today().year + 1, date.today().month, date.today().day)
    lote1 = Lote.objects.create(codigo="LOTE_TEST_3", medicamento=medicamento, cantidad=5000, fecha_vencimiento=fecha_vencimiento)
    lote2 = Lote.objects.create(codigo="LOTE_TEST_4", medicamento=medicamento, cantidad=10000, fecha_vencimiento=fecha_vencimiento)
    Movimiento.objects.create(institucion=institucion, lote=lote1)

    consumo = lote1.cantidad - quiebre.cantidad
    Consumo.objects.create(institucion=institucion, medicamento=medicamento, cantidad=consumo)
    stock = Stock.objects.filter(institucion=institucion, medicamento=medicamento).first()
    assert (
        stock.has_quiebre
    ), "cada consumo debe actualizar el quiebre de stock (stock.cantidad == quiebre.cantidad => stock.has_quiebre=True)"

    Movimiento.objects.create(institucion=institucion, lote=lote2)
    stock = Stock.objects.filter(institucion=institucion, medicamento=medicamento).first()
    assert (
        not stock.has_quiebre
    ), "cada movimiento debe actualizar el quiebre de stock (stock.cantidad == quiebre.cantidad => stock.has_quiebre=True)"


@pytest.mark.django_db
def test_workflow_calculo_caducidad():
    from maestro.models import Institucion, Medicamento
    from stock.models import Lote, Stock, Movimiento
    from .functions import upd_stock_medicamento_institucion

    institucion = Institucion.objects.all().first()
    medicamento = Medicamento.objects.all().first()
    upd_stock_medicamento_institucion()

    fecha_vencimiento = date(date.today().year + 1, date.today().month, date.today().day)
    lote1 = Lote.objects.create(codigo="LOTE_TEST_5", medicamento=medicamento, cantidad=1500, fecha_vencimiento=date.today())
    lote2 = Lote.objects.create(codigo="LOTE_TEST_6", medicamento=medicamento, cantidad=10000, fecha_vencimiento=fecha_vencimiento)
    Movimiento.objects.create(institucion=institucion, lote=lote1)
    Movimiento.objects.create(institucion=institucion, lote=lote2)
    stock = Stock.objects.filter(institucion=institucion, medicamento=medicamento).first()
    # esto corresponde a una simplificación de los ajustes por caducidad
    assert stock.cantidad == 10000, "movimientos de lotes vencidos no deben aumentar la cantidad de stock"
