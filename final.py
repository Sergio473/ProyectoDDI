import machine
import time
import ubinascii
import network
from umqtt.simple import MQTTClient
import dht
import ssd1306

# Configuración de los pines del sensor ultrasónico
trigger_pin = machine.Pin(16, machine.Pin.OUT)
echo_pin = machine.Pin(5, machine.Pin.IN)

# Configurar el buzzer en el pin D8 (GPIO 15)
buzzer_pin = machine.Pin(15, machine.Pin.OUT)
pwm = machine.PWM(buzzer_pin)

# Configurar el botón en el pin D2 (GPIO 4)
button_pin = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)

# Configurar el botón en el pin D5 (GPIO 14)
button_pin2 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

prev_button_value = 1  # Valor previo del botón
# Variable global para almacenar el valor del botón
global_button_value = 0  # Estado inicial (suelto)

# Variable para almacenar el estado anterior del botón
previous_button_state = 1  # Estado inicial (suelto)

# Definir los pines para SCL y SDA
scl_pin = machine.Pin(4)  # D2
sda_pin = machine.Pin(0)  # D3

# Configurar la comunicación I2C
i2c = machine.I2C(scl=scl_pin, sda=sda_pin)

# Configurar la pantalla OLED
pantalla_oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Definir el pin para el sensor de pulso
pulse_pin = machine.Pin(13, machine.Pin.IN)  # Usar el pin D7

# Credenciales de WiFi
ssid = 'Fam.Medina'
password = '1612ANIo435'

# Configuración del servidor MQTT
mqtt_server = '192.168.0.25'
client_id = ubinascii.hexlify(machine.unique_id())
topic_pub = b'gorra'

# Inicializar la conexión WiFi
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while not station.isconnected():
    pass

print('Conexión exitosa')
print(station.ifconfig())

# Conectarse al broker MQTT
try:
    client = MQTTClient(client_id, mqtt_server)
    client.connect()
    print('Conectado al broker MQTT en %s' % mqtt_server)
except OSError as e:
    print('Error al conectar al broker MQTT.')

# Función para enviar un mensaje MQTT
def enviar_mensaje(msg):
    global client
    try:
        client.publish(topic_pub, msg)
    except:
        print("Error al enviar mensaje MQTT")

# Función para medir la distancia con el sensor ultrasónico HC-SR04
def measure_distance():
    trigger_pin.value(0)
    time.sleep_us(2)
    trigger_pin.value(1)
    time.sleep_us(10)
    trigger_pin.value(0)

    while echo_pin.value() == 0:
        pass
    start_time = time.ticks_us()

    while echo_pin.value() == 1:
        pass
    end_time = time.ticks_us()

    pulse_duration = time.ticks_diff(end_time, start_time)

    distance_cm = (pulse_duration * 34300) / (2 * 1000000)
    return distance_cm

# Función para leer el valor del potenciómetro
def leer_potenciometro():
    conversor = machine.ADC(0)  # Pin A0 para el potenciómetro
    pot_value = 1023  # Valor máximo de lectura del ADC

    raw_value = conversor.read()  # Lee el valor del potenciómetro
    tension = int(100 + (raw_value / pot_value) * 200)  # Ajusta el valor en el rango 100-300
    
    return tension

# Función para ajustar el volumen
def adjust_volume():
    pot_value = leer_potenciometro()
    pot_value = map_value(pot_value, 0, 1023, 0, 100)  # Mapear el valor a un rango de 0 a 100
    return pot_value

# Función para activar el buzzer
def activate_buzzer(pot_value):
    pwm.duty(pot_value)  # Establecer el ciclo de trabajo del PWM
    pwm.freq(1000)  # Establecer la frecuencia a 1000 Hz (ajusta según sea necesario)

# Función para desactivar el buzzer
def deactivate_buzzer():
    pwm.duty(0)  # Apagar el buzzer

# Función para cambiar el estado del botón
def toggle_button_state():
    global button_state, prev_button_value
    
    button_value = button_pin.value()  # Leer el valor del botón
    
    if button_value != prev_button_value:
        prev_button_value = button_value
        
        if button_value == 0:  # Si el botón se ha presionado
            if button_state == 0:
                button_state = 1
                return 1
            else:
                button_state = 0
                return 0

# Función para leer la temperatura y humedad
def read_temperature_humidity():
    dht_pin = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)  # Cambia al pin que estás utilizando
    d = dht.DHT11(dht_pin)
    
    d.measure()
    temp_celsius = d.temperature()
    humidity = d.humidity()
    
    temperatura = "{:.2f}°C".format(temp_celsius)
    humedad = "{:.2f}%".format(humidity)
    
    msg = "Temp: " + str(temperatura) + ", Hum: " + str(humedad)
    
    return msg

# Función para verificar el estado del sensor PIR
def check_pir_status():
    pir_pin = machine.Pin(13, machine.Pin.IN)
    pir_status = pir_pin.value()
    return pir_status

# Función para manejar el botón y actualizar la variable global
def check_button():
    global global_button_value, previous_button_state
    button_value = button_pin2.value()
    
    if button_value == 0 and previous_button_state == 1:
        global_button_value = 1 - global_button_value  # Alterna entre 0 y 1
        previous_button_state = 0
    elif button_value == 1:
        previous_button_state = 1

# Función para mostrar un mensaje en la pantalla OLED
def mostrar_mensaje(mensaje, x, y):
    pantalla_oled.fill(0)
    pantalla_oled.text(mensaje, x, y)
    pantalla_oled.show()

# Función para medir el pulso
def medir_pulso(pin):
    contador = 0
    tiempo_inicio = time.ticks_us()

    while pin.value() == 0:
        pass

    while pin.value() == 1:
        pass

    tiempo_fin = time.ticks_us()

    duracion_pulso = time.ticks_diff(tiempo_fin, tiempo_inicio)
    frecuencia = 1000000 / duracion_pulso  # Convertir a Hz
    return frecuencia

def pir_detection():
    # Configuración del sensor PIR
    ir_sensor_pin = machine.Pin(3, machine.Pin.IN)
    
    ir_sensor_status = ir_sensor_pin.value()  # Lee el valor del sensor IR
    
    # Verifica si el sensor IR ha detectado un obstáculo
    if ir_sensor_status == 0:
        return 1
    else:
        return 0
    
    time.sleep(0.1)

# Enviar un mensaje MQTT
try:
    volume_config = 25
    previous_state = None  # Estado previo del botón (inicialmente desconocido)
    
    while True:
        check_button()  # Lee y actualiza el valor del botón
        tension = leer_potenciometro()
        distance = measure_distance()
        
        state_changed = toggle_button_state()  # Llamamos a la función y guardamos el resultado
    
        if state_changed is not None:  # Si el resultado no es None, lo imprimimos
            if state_changed != previous_state:  # Solo imprimimos si ha habido un cambio
                print(state_changed)
                previous_state = state_changed  # Actualizamos el estado previo
            
        # Resto de tu lógica aquí
        time.sleep(0.1)  # Pequeña pausa para evitar lecturas rápidas y fluctuaciones

        print(previous_state)
        if previous_state == 0:
            # Ajustar el volumen y hacer sonar el buzzer durante 1 segundo
            pot_value = adjust_volume()
            volume_config = pot_value
            activate_buzzer(pot_value)
            time.sleep(1)
            deactivate_buzzer()
        else:
            deactivate_buzzer()
            time.sleep(1)
        
        if distance <= tension:
            if global_button_value == 1:
                print("Botón presionado")
                deactivate_buzzer()
            else:
                print("Botón suelto")
                print("Distancia: ", distance)
                print("Volumen:", volume_config)
                activate_buzzer(volume_config)
                print("SONAR PIN")
                time.sleep(1)
        else:
            deactivate_buzzer()
            time.sleep(1)
            print("NADA")
            
        temperature_humidity_msg = read_temperature_humidity()
        
        pir_status = check_pir_status()

        # Verifica si algún PIR ha detectado movimiento
        if pir_status == 1:
            print("¡Movimiento detectado!")
            print("Estado del PIR:", pir_status)
            
        partes_mensaje = temperature_humidity_msg.split(",")  # Dividir el mensaje en partes basadas en las comas
        
        valor_temp = ""
        valor_hum = ""
        if len(partes_mensaje) >= 2:
            valor_temp = partes_mensaje[0]  # Obtener el valor de la temperatura
            valor_hum = partes_mensaje[1] 
            
        pantalla_oled.fill(0)  # Limpiar la pantalla antes de cada muestra
        mostrar_mensaje(valor_temp, 0, 0)  # Mostrar valor de temperatura en la posición (0, 0)
        time.sleep(0.5)
        mostrar_mensaje(valor_hum, 0, 20)  # Mostrar valor de humedad en la posición (0, 20)
        
        valor_numerico_temp = float(valor_temp.split(":")[1].split("°")[0])
        valor_numerico_hum = float(valor_hum.split(":")[1].split("%")[0])
        
        valor_pulso = medir_pulso(pulse_pin)  # Medir el pulso
        
        pir_result = pir_detection()
            
        enviar_mensaje("{" + str(distance) + "," + str(tension) + "," + str(volume_config) + "," + str(previous_state) +
                       "," + str(valor_numerico_temp) +  "," + str(valor_numerico_hum) + "," + str(valor_pulso) + "," + str(pir_result) + "}")
        
        time.sleep(0.1)
        
    
except Exception as e:
    print("Error al enviar mensaje MQTT:", e)

time.sleep(0.1)
