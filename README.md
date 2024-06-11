# <p align="center">GuardianCap</p>

## Objetivo del Proyecto
La gorra con sus sensores y funcionalidades proporcionaría a los invidentes herramientas adicionales para mejorar su seguridad, autonomía y calidad de vida. Con las alarmas, la localización y otras características, la gorra les ayudaría a evitar obstáculos, mantenerse informados sobre su entorno y tomar decisiones más informadas en su vida diaria. Además, la aplicación asociada permitiría una mayor interacción y personalización de la experiencia, brindando a los usuarios un mayor control sobre el uso y las preferencias de la gorra. 
El objetivo es utilizar la tecnología de la gorra y la aplicación asociada para brindar a las personas invidentes herramientas que les ayuden a moverse de manera más segura y confiable en su entorno, brindándoles mayor independencia y calidad de vida.

## Benficiario
- El beneficiario principal de este proyecto sería la comunidad de personas invidentes. 
## Integrantes del Proyecto
- José Israel Saldaña Godínez
- Sergio Abisay Cervantes Sánchez
- Juan Antonio Dominguez Rosales

## Materiales a utlizar 
|ID|Nombre|Descripcion|Imagen|Costo Unitario|Cantidad
|---|---|---|---|---|---|
|1|ESP32|La ESP32 actuaría como el cerebro de la gorra inteligente, gestionando la conectividad, procesando los datos de los sensores y controlando la interacción con otros dispositivos para brindar una experiencia adaptada a las necesidades de las personas sordas.|<img src= "https://m.media-amazon.com/images/I/61eyPE6adjL.jpg" width="500px"/>|$300.00|1|
|2|DHT11|Podría medir la temperatura ambiente. Esto podría ser útil para proporcionar información sobre el clima y la temperatura a la persona sorda, ayudándola a adaptarse y tomar las precauciones necesarias.|<img src= "https://m.media-amazon.com/images/I/61hEppQDiXL._AC_SX466_.jpg" width="500px"/>|$50.00|1|
|3|Sensor de pulso|Podría medir la frecuencia cardíaca de la persona que usa la gorra. Esto podría proporcionar información sobre su nivel de estrés o emoción, y ajustar la configuración de la gorra en consecuencia. Por ejemplo, aumentar la vibración de la gorra si se detecta una frecuencia cardíaca alta, indicando posibles situaciones de emergencia.|<img src= "https://pigra.com.mx/113-large_default/sensor-pulso-cardiaco.jpg" width="500px" width="500px"/>|$60.00|1|
|4|HC-SR04|Puede detectar la presencia de objetos cercanos. Esto podría ser útil para alertar a la persona sorda sobre la presencia de obstáculos o personas cercanas, evitando posibles colisiones.|<img src= "https://sonrobots.com/wp-content/uploads/2021/01/HCSR04.jpg" width="500px"/>|$50.00|1|
|5|MPU-6050|Puede detectar la aceleración y la orientación de la cabeza. Esto podría ser útil para detectar movimientos específicos de la cabeza, como inclinaciones o sacudidas, y utilizarlos como comandos para controlar la gorra inteligente o realizar acciones específicas.|<img src= "https://m.media-amazon.com/images/I/51LBN+6GpbL._SX342_SY445_.jpg" width="500px"/>|$60.00|1|
|6|INMP441|Podría utilizarse para captar el sonido ambiente y enfocarse en la dirección de interés, como la persona que está hablando. Esto ayudaría a filtrar el ruido no deseado y mejorar la calidad del audio capturado.|<img src= "https://ae01.alicdn.com/kf/H35aa6e2af11f4944be289ae274777688O.jpg_640x640q90.jpg" width="500px"/>|$50.00|1|
|7|RaspberryPi|Complementa la funcionalidad de la ESP32 al ofrecer un mayor poder de procesamiento, conectividad y capacidades de interfaz de usuario en el proyecto de una gorra inteligente para personas sordas. Su versatilidad y capacidades ampliadas permiten realizar tareas más complejas y aprovechar servicios en línea para mejorar la experiencia y funcionalidad del dispositivo.|<img src= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNsrkqdk7i9F5jgBcOOqvA0FBuWZd5PpXhN4Ryk4J5MrlvST15DCTHT46_4W_OPZrnZEw&usqp=CAU" width="500px"/>|$3000.00|1|

## Tabla de Software utilizado
| ID  | Software               | Versión | Tipo                                                 |
|----|----------|---------|------|
| 01  | Fritzing               | 0.9.3   | Diseño de circuitos (licencia libre)                |
| 03  | Micro Python           | 3.11.3  | Lenguaje de programación (licencia libre)          |
| 04  | Github                 | N/A     | Plataforma de alojamiento (licencia libre)          |
| 05  | PySerial               | 3.4     | Librería para el sensor de pulso cardíaco (licencia libre) |
| 06  | Adafruit CircuitPython | 4.0     | Librería para el sensor de temperatura y humedad del cuerpo humano |
| 07  | RPi.GPIO               | 0022    | Librería para sensor ultrasónico (licencia libre)    |
| 08  | VL53L0X                | 1.0.4   | Librería python para el manejo del sensor láser para distancia VL53L0X |
| 09  | mpu6050                | 1.0.1   | Librería python para el manejo del sensor acelerómetro mpu6050 |
| 10  | openHASP               | 0.7.0-rc4 | Reimplementación del boceto HASwitchPlate optimizado con LVGL |
| 11  | Node-Red |   3.0.2 |Software Libre |
| 12  | Raspberry-Pi |  Raspberry Pi 4 | Pequeño computador que corre un sistema operativo linux|


## Tabla de historias de usuario
| Id | Historia de usuario | Prioridad | Estimación | Como probarlo | Responsable |
|----|---------------------|-----------|------------|---------------|-------------|
|GCP001|Como invidente, quiero poder detectar obstáculos en mi camino mientras uso la gorra para evitar accidentes.|Debe|1 dia|Se puede probar colocando obstáculos en el camino del usuario y verificar si la gorra emite una señal de advertencia o vibra para alertar al usuario sobre la presencia del obstáculo.|Sergio |
|GCP002|Como invidente, quiero poder ajustar el tamaño de la gorra para que se ajuste correctamente a mi cabeza.|Debe|1 dias|Se puede probar proporcionando diferentes tamaños de gorra y verificar si el usuario puede ajustarla correctamente para obtener un ajuste cómodo y seguro.|Sergio|
|GCP003|Como invidente, quiero poder recibir información sobre la ubicación de objetos cercanos a mí mientras uso la gorra.|Debe|2 dias|Se puede probar colocando objetos a diferentes distancias del usuario y verificar si la gorra emite señales o vibraciones proporcionales a la proximidad de los objetos.|Israel|
|GCP004|Como invidente, quiero recibir información sobre la temperatura y la humedad actual cada cierto tiempo mientras uso la gorra.|Debe|3 dias|Se puede probar conectando la gorra a una fuente de datos meteorológicos y verificar si la gorra proporciona información hablada o mediante vibraciones sobre el clima actual.|Israel|
|GCP005| Como invidente, quiero recibir alertas de humedad para saber si debo tomar precauciones adicionales en caso de lluvia o condiciones húmedas mientras uso la gorra.|Debe|3 dias|Se puede probar exponiendo la gorra a diferentes niveles de humedad y verificar si emite una alerta sonora cuando la humedad alcanza cierto umbral.|Antonio|
|GCP06|Como invidente, quiero poder ajustar la sensibilidad del sensor de distancia en la gorra para adaptarlo a mis necesidades y entorno.|Debe|2 dias|Se puede probar ajustando la sensibilidad del sensor de distancia en la gorra y verificar si las alarmas se activan adecuadamente cuando el usuario se acerca a objetos o paredes.|Antonio|
|GCP07|Como invidente, quiero poder ajustar el volumen de las alarmas en la gorra para adaptarlo a mis preferencias auditivas.|Debe|1 dia|Se puede probar ajustando el volumen de las alarmas en la gorra y verificar si el usuario puede escucharlas claramente sin que sean demasiado fuertes o suaves.|Antonio|
|GCP08|Como invidente, quiero poder silenciar temporalmente las alarmas en la gorra cuando sea necesario.|Debe|2 dias|Se puede probar activando una alarma en la gorra y luego verificar si el usuario puede silenciarla temporalmente sin desactivarla por completo.|Sergio|
|GCP09|Como invidente, quiero saber mi pulso cardiaco en un dashboard para que los demas tambien lo puedan ver.|Debe|2 dias|Se probara viendo que el sensor mande la informacion correcta a la pantalla de acuerdo al pulso del usuario.|Israel|



## Prototipo en dibujo
<img src="https://github.com/AlexAlonRo/ProyectoDDI/assets/89074060/78244930-364e-462c-b222-e3e46d67b43e" width="300" height="200"/>

## Placa PCB
<img src="https://github.com/AlexAlonRo/ProyectoDDI/assets/105385260/699a4b2a-ebd2-43e6-a7c6-5d85e00df0c2" width="800" height="400"/>


## Prototipo en 3D
### Enlace Tinkercad
https://www.tinkercad.com/things/hey5mWPRRYn-incredible-rottis/edit?sharecode=QkGc5UIvuHH8nqbjJAFoY8htMV52TlNGm9aqxtM-Xoo

### Imagen del prototipo 3D
<img src="https://github.com/AlexAlonRo/ProyectoDDI/assets/48026299/fc6d6237-2116-4e25-a74a-f906672e2019" width="800" height="400"/>

# Evidencia del Sprint 1
## Implementacion de la base de datos Maria DB
![image]()

## Lecturas de en consola de la pantalla ESP32

# Evidencia del Sprint 2

## Diseño de la carcasa en MDF

## Imagenes del Casco

## Desplieqgue del Dashboard

## Implementación de Sensores y Actuadores

## Comunicación MQTT entre Dispositivos

## Base de Datos

## Carta del beneficiario

