from controller import Robot, DistanceSensor, LightSensor
import math

robot = Robot()
timestep = int(robot.getBasicTimeStep())

# --- Inicialización de motores ---
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# --- Inicialización y habilitación de sensores ---
# IMPORTANTE: Asegúrate de que los nombres de los dispositivos ('ps7', 'ls6')
# coincidan exactamente con los nombres de los nodos de los sensores en tu modelo de e-puck en Webots.
distance_sensor_front = robot.getDevice('ps7')
distance_sensor_front.enable(timestep)
light_sensor = robot.getDevice('ls6')
light_sensor.enable(timestep)

EPUCK_WHEEL_DISTANCE = 0.052 # Distancia entre las ruedas en metros
EPUCK_WHEEL_RADIUS = 0.0205 # Radio de las ruedas en metros
DEFAULT_ANGULAR_SPEED = 2.0 # Velocidad por defecto para giros por ángulo

def avanzar(velocidad, duracion_ms):
    print(f"[ACCION] Avanzando a velocidad {velocidad:.2f} por {duracion_ms}ms")
    duracion_s = duracion_ms / 1000.0
    left_motor.setVelocity(velocidad)
    right_motor.setVelocity(velocidad)
    tiempo_inicial = robot.getTime()
    while robot.step(timestep) != -1 and (robot.getTime() - tiempo_inicial) < duracion_s:
        pass
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)

def retroceder(velocidad, duracion_ms):
    print(f"[ACCION] Retrocediendo a velocidad {velocidad:.2f} por {duracion_ms}ms")
    duracion_s = duracion_ms / 1000.0
    left_motor.setVelocity(-velocidad)
    right_motor.setVelocity(-velocidad)
    tiempo_inicial = robot.getTime()
    while robot.step(timestep) != -1 and (robot.getTime() - tiempo_inicial) < duracion_s:
        pass
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)

def girar(direccion, velocidad, duracion_ms):
    print(f"[ACCION] Girando (tiempo) {direccion} a velocidad {velocidad:.2f} por {duracion_ms}ms")
    duracion_s = duracion_ms / 1000.0
    if direccion == 'IZQUIERDA':
        left_motor.setVelocity(-velocidad)
        right_motor.setVelocity(velocidad)
    elif direccion == 'DERECHA':
        left_motor.setVelocity(velocidad)
        right_motor.setVelocity(-velocidad)
    tiempo_inicial = robot.getTime()
    while robot.step(timestep) != -1 and (robot.getTime() - tiempo_inicial) < duracion_s:
        pass
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)

def girar_angulo_simple(direccion, angulo_grados):
    print(f"[ACCION] Girando (ángulo) {direccion} {angulo_grados:.2f} grados (velocidad por defecto)")
    velocidad_motor = DEFAULT_ANGULAR_SPEED
    
    angulo_rad = math.radians(angulo_grados)
    
    velocidad_angular_robot = (2 * velocidad_motor * EPUCK_WHEEL_RADIUS) / EPUCK_WHEEL_DISTANCE
    
    duracion_s = 0
    if velocidad_angular_robot != 0:
        duracion_s = angulo_rad / velocidad_angular_robot
    
    if direccion == 'IZQUIERDA':
        left_motor.setVelocity(-velocidad_motor)
        right_motor.setVelocity(velocidad_motor)
    elif direccion == 'DERECHA':
        left_motor.setVelocity(velocidad_motor)
        right_motor.setVelocity(-velocidad_motor)
    
    tiempo_inicial = robot.getTime()
    while robot.step(timestep) != -1 and (robot.getTime() - tiempo_inicial) < duracion_s:
        pass
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)

def esperar(duracion_ms):
    print(f"[ACCION] Esperando por {duracion_ms}ms")
    duracion_s = duracion_ms / 1000.0
    tiempo_inicial = robot.getTime()
    while robot.step(timestep) != -1 and (robot.getTime() - tiempo_inicial) < duracion_s:
        pass

def get_sensor_value(sensor_name):
    value = 0.0
    if sensor_name == 'light':
        value = light_sensor.getValue()
        print(f"[SENSOR] Luz: {value:.2f}")
    elif sensor_name == 'distance':
        value = distance_sensor_front.getValue()
        print(f"[SENSOR] Distancia: {value:.2f}")
    else:
        print(f"[SENSOR ERROR] Sensor desconocido: {sensor_name}")
    return value

if __name__ == '__main__':
    print('Iniciando controlador generado por Blockly')
    # Inicio del programa del robot
    avanzar(3, 1000)
    for _ in range(2):
        if get_sensor_value('distance') > 500:
            girar_angulo_simple('IZQUIERDA', 90)
            avanzar(1, 1500)
        retroceder(2, 700)
        esperar(200)
    print('FINALIZAR comando ejecutado')
    while robot.step(timestep) != -1:
        pass