# Taller de Software

## Contexto

Este repositorio fue creado a partir de una plantilla de trabajo que solamente tiene instalado Django y las dependencias requeridas para este módulo.

Usted y su célula de trabajo forman parte del área de desarrollo a cargo de la implementación de este módulo. Además de su célula, existe otra a cargo de la implementación de los *tests* que su proyecto debe superar.


## Instrucciones

El líder de desarrollo debe crear un *fork* de este repositorio y otorgar acceso a los demás miembros de la célula. Se utilizará una metodología de trabajo basada en GitFlow.

Se utilizará la rama _release_ para integrar los aportes de todas las células. Deben revisar de manera periódica en GitHub que la rama _release_ de su _fork_ esté sincronizada con el repositorio principal. 

Cada actualización de la rama _release_ traerá consigo código mockeado y pytests que su célula deberá implementar.

El líder de desarrollo debe crear la rama _develop_ en el _fork_ de la célula a partir de la rama _release_ y encargarse de mantenerla actualizada desde _release_. 

El líder de desarrollo deberá enviar el código en _develop_ a la rama _release_ de su _fork_ cuando todos los tests disponibles se ejecuten correctamente, el código esté formateado correctamente y no tenga malas prácticas de codificación (black y flake8). 

Deberá además dar aviso a través del **sistema de mensajería** (foro de u-cursos) que el equipo ya terminó con los tests asignados.
