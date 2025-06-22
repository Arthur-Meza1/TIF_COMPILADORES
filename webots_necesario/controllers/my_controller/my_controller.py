from controller import Robot

# Crear instancia del robot
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Obtener los motores
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Configurar motores para velocidad continua
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Inicializar sensores de proximidad (ps0 a ps7)
ps = []
for i in range(8):
    sensor = robot.getDevice(f'ps{i}')
    sensor.enable(timestep)
    ps.append(sensor)

# Función para avanzar por una duración dada
def avanzar(velocidad, duracion_ms):
    duracion = duracion_ms / 1000.0
    left_motor.setVelocity(velocidad)
    right_motor.setVelocity(velocidad)
    tiempo_inicial = robot.getTime()
    while robot.step(timestep) != -1 and (robot.getTime() - tiempo_inicial) < duracion:
        pass
    detener()

# Función para girar por una duración dada
def girar(direccion, velocidad, duracion_ms):
    duracion = duracion_ms / 1000.0
    if direccion == 'IZQUIERDA':
        left_motor.setVelocity(-velocidad)
        right_motor.setVelocity(velocidad)
    elif direccion == 'DERECHA':
        left_motor.setVelocity(velocidad)
        right_motor.setVelocity(-velocidad)
    tiempo_inicial = robot.getTime()
    while robot.step(timestep) != -1 and (robot.getTime() - tiempo_inicial) < duracion:
        pass
    detener()

# Función para detener
def detener():
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)

# Función para esperar sin moverse
def esperar(duracion_ms):
    duracion = duracion_ms / 1000.0
    tiempo_inicial = robot.getTime()
    while robot.step(timestep) != -1 and (robot.getTime() - tiempo_inicial) < duracion:
        pass

# Función para leer sensores frontales (ps6 y ps7)
def obstaculo_frontal():
    front_left = ps[6].getValue()
    front_right = ps[7].getValue()
    print(f"Sensor ps6: {front_left:.2f} | Sensor ps7: {front_right:.2f}")
    return front_left > 80 or front_right > 80  # Ajusta el umbral según tu escenario

# Programa principal
if __name__ == '__main__':
    print("Iniciando controlador con funciones y sensores")
    print("INICIAR comando ejecutado")

    avanzar(3.0, 2000)
    esperar(500)

    # Evitar obstáculos con sensores
    for _ in range(10):  # 10 ciclos de evaluación
        if obstaculo_frontal():
            print("Obstáculo detectado: girando a la derecha")
            girar('DERECHA', 2.0, 1000)
        else:
            print("Camino libre: avanzando")
            avanzar(3.0, 1000)
        esperar(200)

    print("FINALIZAR comando ejecutado")

    # Mantener el robot activo al final
    while robot.step(timestep) != -1:
        pass
