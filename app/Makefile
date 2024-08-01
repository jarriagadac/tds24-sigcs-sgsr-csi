# makefile

venv:
	python3 -m venv ../venv

init:
	pip install --upgrade pip
	pip install -r requirements.txt
	rm -f db.sqlite3
	make migrate
	make loaddata

loaddata:
	python manage.py loaddata _fixtures/auth_user.json
	python manage.py loaddata _fixtures/maestro_institucion.json
	python manage.py loaddata _fixtures/maestro_medicamento.json
	python manage.py loaddata _fixtures/maestro_item.json
	python manage.py loaddata _fixtures/maestro_equipamiento.json
	python manage.py loaddata _fixtures/maestro_quiebre.json
	# python manage.py loaddata _fixtures/stock.json

dumpdata:
	python manage.py dumpdata auth.user --indent 2 > _fixtures/auth_user.json
	python manage.py dumpdata maestro.institucion --indent 2 > _fixtures/maestro_institucion.json
	python manage.py dumpdata maestro.medicamento --indent 2 > _fixtures/maestro_medicamento.json
	python manage.py dumpdata maestro.item --indent 2 > _fixtures/maestro_item.json
	python manage.py dumpdata maestro.equipamiento --indent 2 > _fixtures/maestro_equipamiento.json
	python manage.py dumpdata maestro.quiebre --indent 2 > _fixtures/maestro_quiebre.json
	python manage.py dumpdata stock --indent 2 > _fixtures/stock.json

precommit:
	black --line-length=140 .
	flake8 --ignore E501 .

migrations:
	rm -f stock/migrations/000*.py
	python manage.py makemigrations stock
	make precommit

migrate:
	rm -f db.sqlite3
	python manage.py migrate

update:
	pur -r requirements.txt

run:
	python manage.py runserver 0.0.0.0:8000

__test_prepare:
	rm -f stock/migrations/000*.py
	python manage.py makemigrations stock

run_tests:
	make __test_prepare
	pytest -vv


run_tests_basicos:
	make __test_prepare
	pytest -vv -k "_b_"

run_tests_intermedios:
	make __test_prepare
	pytest -vv -k "_i_"

run_tests_avanzados:
	make __test_prepare
	pytest -vv -k "_a_"