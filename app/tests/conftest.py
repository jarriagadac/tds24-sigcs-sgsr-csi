import pytest

from django.core.management import call_command


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("loaddata", "_fixtures/maestro_institucion.json")
        call_command("loaddata", "_fixtures/maestro_medicamento.json")
        call_command("loaddata", "_fixtures/maestro_item.json")
        call_command("loaddata", "_fixtures/maestro_equipamiento.json")
        call_command("loaddata", "_fixtures/maestro_quiebre.json")

        try:
            call_command("loaddata", "_fixtures/stock.json")
        except Exception:
            pass
