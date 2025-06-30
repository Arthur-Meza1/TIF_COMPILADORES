# robot_controller.py - Generador de código Python para el controlador de Webots

import math

# Parámetros del e-puck para el cálculo del giro (valores típicos)
EPUCK_WHEEL_DISTANCE = 0.052 # Distancia entre las ruedas en metros
EPUCK_WHEEL_RADIUS = 0.0205  # Radio de las ruedas en metros

# Velocidad por defecto para el giro por ángulo (GIRAR_ANGULO)
DEFAULT_ANGULAR_SPEED = 2.0 # rad/s, un valor común para el e-puck

def generar_codigo(comandos_ast, indent_level=0):
    """
    Genera el código Python para el controlador de Webots a partir del AST de comandos.
    indent_level maneja la indentación para bloques anidados.
    """
    python_code_lines = []
    current_indent_str = "    " * indent_level

    if indent_level == 0:
        python_code_lines.append("from controller import Robot, DistanceSensor, LightSensor")
        python_code_lines.append("import math")

        python_code_lines.append("")
        python_code_lines.append("robot = Robot()")
        python_code_lines.append("timestep = int(robot.getBasicTimeStep())")
        python_code_lines.append("")
        python_code_lines.append("# --- Inicialización de motores ---")
        python_code_lines.append("left_motor = robot.getDevice('left wheel motor')")
        python_code_lines.append("right_motor = robot.getDevice('right wheel motor')")
        
        left_motor_velocity_default = 0.0
        right_motor_velocity_default = 0.0
        python_code_lines.append("left_motor.setPosition(float('inf'))")
        python_code_lines.append("right_motor.setPosition(float('inf'))")
        python_code_lines.append(f"left_motor.setVelocity({left_motor_velocity_default})")
        python_code_lines.append(f"right_motor.setVelocity({right_motor_velocity_default})")
        python_code_lines.append("")
        
        python_code_lines.append("# --- Inicialización y habilitación de sensores ---")
        python_code_lines.append("# IMPORTANTE: Asegúrate de que los nombres de los dispositivos ('ps7', 'ls6')")
        python_code_lines.append("# coincidan exactamente con los nombres de los nodos de los sensores en tu modelo de e-puck en Webots.")
        
        python_code_lines.append("distance_sensor_front = robot.getDevice('ps7')")
        python_code_lines.append("distance_sensor_front.enable(timestep)")
        
        python_code_lines.append("light_sensor = robot.getDevice('ls6')")
        python_code_lines.append("light_sensor.enable(timestep)")
        python_code_lines.append("")

        # --- Parámetros físicos del robot para cálculos de giro ---
        python_code_lines.append(f"EPUCK_WHEEL_DISTANCE = {EPUCK_WHEEL_DISTANCE} # Distancia entre las ruedas en metros")
        python_code_lines.append(f"EPUCK_WHEEL_RADIUS = {EPUCK_WHEEL_RADIUS} # Radio de las ruedas en metros")
        python_code_lines.append(f"DEFAULT_ANGULAR_SPEED = {DEFAULT_ANGULAR_SPEED} # Velocidad por defecto para giros por ángulo")
        python_code_lines.append("")

        # Funciones auxiliares de control de robot
        python_code_lines.append("def avanzar(velocidad, duracion_ms):")
        python_code_lines.append(f"    print(f\"[ACCION] Avanzando a velocidad {{velocidad:.2f}} por {{duracion_ms}}ms\")")
        python_code_lines.append("    duracion_s = duracion_ms / 1000.0")
        python_code_lines.append("    left_motor.setVelocity(velocidad)")
        python_code_lines.append("    right_motor.setVelocity(velocidad)")
        python_code_lines.append("    tiempo_inicial = robot.getTime()")
        python_code_lines.append("    while robot.step(timestep) != -1 and (robot.getTime() - tiempo_inicial) < duracion_s:")
        python_code_lines.append("        pass")
        python_code_lines.append("    left_motor.setVelocity(0)")
        python_code_lines.append("    right_motor.setVelocity(0)")
        python_code_lines.append("")

        python_code_lines.append("def retroceder(velocidad, duracion_ms):")
        python_code_lines.append(f"    print(f\"[ACCION] Retrocediendo a velocidad {{velocidad:.2f}} por {{duracion_ms}}ms\")")
        python_code_lines.append("    duracion_s = duracion_ms / 1000.0")
        python_code_lines.append("    left_motor.setVelocity(-velocidad)")
        python_code_lines.append("    right_motor.setVelocity(-velocidad)")
        python_code_lines.append("    tiempo_inicial = robot.getTime()")
        python_code_lines.append("    while robot.step(timestep) != -1 and (robot.getTime() - tiempo_inicial) < duracion_s:")
        python_code_lines.append("        pass")
        python_code_lines.append("    left_motor.setVelocity(0)")
        python_code_lines.append("    right_motor.setVelocity(0)")
        python_code_lines.append("")
        
        python_code_lines.append("def girar(direccion, velocidad, duracion_ms):")
        python_code_lines.append(f"    print(f\"[ACCION] Girando (tiempo) {{direccion}} a velocidad {{velocidad:.2f}} por {{duracion_ms}}ms\")")
        python_code_lines.append("    duracion_s = duracion_ms / 1000.0")
        python_code_lines.append("    if direccion == 'IZQUIERDA':")
        python_code_lines.append("        left_motor.setVelocity(-velocidad)")
        python_code_lines.append("        right_motor.setVelocity(velocidad)")
        python_code_lines.append("    elif direccion == 'DERECHA':")
        python_code_lines.append("        left_motor.setVelocity(velocidad)")
        python_code_lines.append("        right_motor.setVelocity(-velocidad)")
        python_code_lines.append("    tiempo_inicial = robot.getTime()")
        python_code_lines.append("    while robot.step(timestep) != -1 and (robot.getTime() - tiempo_inicial) < duracion_s:")
        python_code_lines.append("        pass")
        python_code_lines.append("    left_motor.setVelocity(0)")
        python_code_lines.append("    right_motor.setVelocity(0)")
        python_code_lines.append("")

        python_code_lines.append("def girar_angulo_simple(direccion, angulo_grados):")
        python_code_lines.append(f"    print(f\"[ACCION] Girando (ángulo) {{direccion}} {{angulo_grados:.2f}} grados (velocidad por defecto)\")")
        python_code_lines.append("    velocidad_motor = DEFAULT_ANGULAR_SPEED")
        python_code_lines.append("    ")
        python_code_lines.append("    angulo_rad = math.radians(angulo_grados)")
        python_code_lines.append("    ")
        python_code_lines.append("    velocidad_angular_robot = (2 * velocidad_motor * EPUCK_WHEEL_RADIUS) / EPUCK_WHEEL_DISTANCE")
        python_code_lines.append("    ")
        python_code_lines.append("    duracion_s = 0")
        python_code_lines.append("    if velocidad_angular_robot != 0:")
        python_code_lines.append("        duracion_s = angulo_rad / velocidad_angular_robot")
        python_code_lines.append("    ")
        python_code_lines.append("    if direccion == 'IZQUIERDA':")
        python_code_lines.append("        left_motor.setVelocity(-velocidad_motor)")
        python_code_lines.append("        right_motor.setVelocity(velocidad_motor)")
        python_code_lines.append("    elif direccion == 'DERECHA':")
        python_code_lines.append("        left_motor.setVelocity(velocidad_motor)")
        python_code_lines.append("        right_motor.setVelocity(-velocidad_motor)")
        python_code_lines.append("    ")
        python_code_lines.append("    tiempo_inicial = robot.getTime()")
        python_code_lines.append("    while robot.step(timestep) != -1 and (robot.getTime() - tiempo_inicial) < duracion_s:")
        python_code_lines.append("        pass")
        python_code_lines.append("    left_motor.setVelocity(0)")
        python_code_lines.append("    right_motor.setVelocity(0)")
        python_code_lines.append("")
        
        python_code_lines.append("def esperar(duracion_ms):")
        python_code_lines.append(f"    print(f\"[ACCION] Esperando por {{duracion_ms}}ms\")")
        python_code_lines.append("    duracion_s = duracion_ms / 1000.0")
        python_code_lines.append("    tiempo_inicial = robot.getTime()")
        python_code_lines.append("    while robot.step(timestep) != -1 and (robot.getTime() - tiempo_inicial) < duracion_s:")
        python_code_lines.append("        pass")
        python_code_lines.append("")
        
        python_code_lines.append("def get_sensor_value(sensor_name):")
        python_code_lines.append("    value = 0.0")
        python_code_lines.append("    if sensor_name == 'light':")
        python_code_lines.append("        value = light_sensor.getValue()")
        python_code_lines.append(f"        print(f\"[SENSOR] Luz: {{value:.2f}}\")")
        python_code_lines.append("    elif sensor_name == 'distance':")
        python_code_lines.append("        value = distance_sensor_front.getValue()")
        python_code_lines.append(f"        print(f\"[SENSOR] Distancia: {{value:.2f}}\")")
        python_code_lines.append("    else:")
        python_code_lines.append(f"        print(f\"[SENSOR ERROR] Sensor desconocido: {{sensor_name}}\")")
        python_code_lines.append("    return value")
        python_code_lines.append("")

        python_code_lines.append("if __name__ == '__main__':")
        python_code_lines.append("    print('Iniciando controlador generado por Blockly')")
        python_code_lines.append("    # Inicio del programa del robot")

        filtered_commands_ast = [cmd for cmd in comandos_ast if cmd['command'] not in ['FINALIZAR', 'INICIAR']]
        
        python_code_lines.extend(generar_codigo(filtered_commands_ast, indent_level + 1))
        
        python_code_lines.append("    print('FINALIZAR comando ejecutado')")
        python_code_lines.append("    while robot.step(timestep) != -1:")
        python_code_lines.append("        pass")
        return python_code_lines

    for command_dict in comandos_ast:
        cmd_name = command_dict['command']

        if cmd_name == "INICIAR":
            pass
        elif cmd_name == "AVANZAR":
            duration = command_dict['duration']
            speed = command_dict['speed']
            python_code_lines.append(f"{current_indent_str}avanzar({speed}, {duration})")
        elif cmd_name == "RETROCEDER":
            duration = command_dict['duration']
            speed = command_dict['speed']
            python_code_lines.append(f"{current_indent_str}retroceder({speed}, {duration})")
        elif cmd_name == "GIRAR":
            direction = command_dict['direction']
            speed = command_dict['speed']
            duration = command_dict['duration']
            python_code_lines.append(f"{current_indent_str}girar('{direction}', {speed}, {duration})")
        elif cmd_name == "GIRAR_ANGULO":
            direction = command_dict['direction']
            angle = command_dict['angle']
            python_code_lines.append(f"{current_indent_str}girar_angulo_simple('{direction}', {angle})")
        elif cmd_name == "ESPERAR":
            duration = command_dict['duration']
            python_code_lines.append(f"{current_indent_str}esperar({duration})")
        elif cmd_name == "FINALIZAR":
            pass
        elif cmd_name == "SI":
            condition = command_dict['condition']
            
            left_val = ""
            if isinstance(condition['left'], dict) and condition['left'].get('type') == 'sensor':
                left_val = f"get_sensor_value('{condition['left']['name']}')"
            else:
                left_val = str(condition['left'])

            right_val = ""
            if isinstance(condition['right'], dict) and condition['right'].get('type') == 'sensor':
                right_val = f"get_sensor_value('{condition['right']['name']}')"
            else:
                right_val = str(condition['right'])

            op_map = {
                "IGUAL": "==", "DIFERENTE": "!=", "MENOR": "<",
                "MENOR_IGUAL": "<=", "MAYOR": ">", "MAYOR_IGUAL": ">="
            }
            operator_sym = op_map.get(condition['operator'], "==")

            python_code_lines.append(f"{current_indent_str}if {left_val} {operator_sym} {right_val}:")
            python_code_lines.extend(generar_codigo(command_dict['body'], indent_level + 1))
        elif cmd_name == "REPETIR":
            times = command_dict['times']
            python_code_lines.append(f"{current_indent_str}for _ in range({times}):")
            python_code_lines.extend(generar_codigo(command_dict['body'], indent_level + 1))
        else:
            python_code_lines.append(f"{current_indent_str}# ERROR: Command '{cmd_name}' not recognized or malformed in AST.")

    return python_code_lines
