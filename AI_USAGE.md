# Uso de Inteligencia Artificial en este Proyecto

## Herramienta utilizada

**ChatGPT (OpenAI)**

## Archivo

**app.py**

## Prompt utilizado

Genera un programa en Python que permita sumar dos números utilizando funciones, valide que el usuario ingrese únicamente valores numéricos mediante manejo de excepciones (`try` y `except`) y permita realizar múltiples operaciones hasta que el usuario decida salir del programa.

## Código generado por IA

La inteligencia artificial fue utilizada como apoyo para generar una primera versión del programa, incluyendo la estructura básica con funciones, validación de entradas, manejo de errores y repetición del proceso mediante un ciclo.

## Cambios realizados

Después de generar el código con la IA, se realizó una revisión completa y se efectuaron las siguientes mejoras:

- Se revisó la lógica de la función `sumar()` para garantizar que realizara correctamente la operación matemática.
- Se implementó una función independiente (`pedir_numero()`) para validar la entrada de datos utilizando `try` y `except`, evitando que el programa finalice por errores al ingresar información no numérica.
- Se estructuró el programa dentro de la función `main()` para mejorar la organización y facilitar su mantenimiento.
- Se agregó un ciclo `while` que permite al usuario realizar múltiples sumas sin necesidad de ejecutar nuevamente el programa.
- Se incorporó una opción para finalizar la ejecución de forma controlada mediante la respuesta del usuario.
- Se mejoraron los mensajes mostrados en pantalla para hacer la interacción más clara y amigable.
- Se realizaron pruebas manuales con diferentes datos válidos e inválidos para verificar el correcto funcionamiento del programa.

## Justificación

La inteligencia artificial fue utilizada como una herramienta de apoyo durante el desarrollo del programa, mas no como un sustituto del proceso de aprendizaje. Todo el código generado fue revisado, comprendido y evaluado antes de ser incorporado al proyecto. Además, se realizaron modificaciones para mejorar la organización, la validación de datos y la experiencia del usuario, asegurando que el resultado final cumpliera con buenas prácticas de programación.

## Política de uso

Todo el código asistido por inteligencia artificial fue analizado, comprendido, probado y adaptado antes de ser utilizado en el proyecto. La responsabilidad sobre el funcionamiento, las modificaciones realizadas y la documentación presentada corresponde íntegramente al estudiante.