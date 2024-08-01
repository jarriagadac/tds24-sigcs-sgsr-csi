def upd_stock_medicamento_institucion():
    from maestro.models import Institucion, Medicamento
    from stock.models import Stock, Movimiento, Consumo

    # aseguro que no haya movimientos, consumos ni stock
    Movimiento.objects.all().delete()
    Consumo.objects.all().delete()
    Stock.objects.all().delete()

    for i in Institucion.objects.all():
        for m in Medicamento.objects.all():
            s, _ = Stock.objects.get_or_create(institucion=i, medicamento=m)
