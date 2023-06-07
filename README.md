# Automatización de lecturas NFC con un manipulador de 5 grados de libertad

## Introducción
Este proyecto trata sobre la automatización de lecturas NFC utilizando un manipulador de 5 grados de libertad para aplicaciones en robótica de servicios. El objetivo es desarrollar un sistema que permita la detección automática y fiable de objetos de interés, como medicamentos, para ayudar a personas mayores.

## Estructura del repositorio
- `nfc_sensor`: Este directorio contiene subcarpetas relacionadas con el sensor NFC:
  - `nfc_sensor_code`: Aquí encontrarás el código para leer y escribir en las etiquetas NFC utilizando el módulo de lectura y escritura NFC.
  - `nfc_sensor_CAD`: Este directorio contiene los archivos CAD relacionados con el sensor NFC.
  - `nfc_sensor_tags`: Aquí encontrarás la estructura JSON para las etiquetas NFC, incluyendo la definición de los datos que se almacenarán en las etiquetas, como el nombre del medicamento, la dosis y la fecha de caducidad.
- `mobile_app`: Este directorio contiene la APK del prototipo de aplicación móvil que permite a los cuidadores de la persona dependiente escribir en las NFC tags.
- `interbotix_ws`: Aquí encontrarás el código relacionado con el workspace de ROS para el robot. Este workspace está basado en el proporcionado por el fabricante Interbotix (https://github.com/Interbotix).
- `python_scripts`: Aquí encontrarás scripts en Python que demuestran la funcionalidad del robot.
