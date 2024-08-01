# Taller de Software

## Ambiente de Desarrollo

El primer paso para tener éxito en la fase de implementación es contar con un ambiente de desarrollo bien configurado.

- Clona este repositorio utilizando GitHub Desktop.
- Desde GitHub Desktop abre Visual Studio Code.
- Abre un Terminal en Visual Studio Code.
- Crea y activa un virtualenv de Python. Virtualenv te permite instalar paquetes de Python, utilizando la herramienta *pip*, de forma que estos quedan disponibles sólo para este proyecto.

```console
disw@DCC ~/ $ python3 -m venv venv
disw@DCC ~/ $ source venv/bin/activate
```

- Inicializa el proyecto. En la carpeta app encontrarás un archivo Makefile; este se utiliza para automatizar algunos comandos que se utilizarán de manera recurrente durante el desarrollo.

```console
disw@DCC ~/ (venv) $ cd app
disw@DCC ~/app/ (venv) $ make init
```

- Ejecuta el servidor de desarrollo de Django y verifica en un browser que esté funcionando correctamente.

```console
disw@DCC ~/app/ (venv) $ make run
```

Si ves el logo de Django en el browser significa que el ambiente de desarrollo está funcionando correctamente.

- Correr los tests y comenzar a implementar el código necesario para que aprueben.

```console
disw@DCC ~/app/ (venv) $ make run_tests
```

### Comandos disponibles:

- **make venv**: crea un virtualenv en la carpeta venv en la raíz del proyecto.
- **make init**: actualiza la versión de *pip* de tu virtualenv, instala las dependencias del proyecto presentes en el archivo requirements.txt, elimina la base de datos db.sqlite3 si existe, corre las migraciones de Django y carga data de prueba.
- **make precommit**: formatea los archivos .py utilizando *black* y luego ejecuta el linter *flake8* para revisar que se cumplan buenas prácticas de codificación.
- **make run_tests**: ejecuta los todos los tests del proyecto utilizando pytest.
