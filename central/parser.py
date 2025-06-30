# parser.py - Analizador sintáctico para los tokens del lexer

import re

def parser(tokens):
    """
    Toma una lista de tokens del lexer y construye una estructura de comandos anidada (AST).
    Maneja bloques SI y REPETIR con su nueva estructura.
    """
    program_ast = []
    scope_stack = [program_ast]

    def parse_arg_value(arg_str):
        if isinstance(arg_str, dict):
            return arg_str
        if str(arg_str).upper() == 'SENSOR_LUZ':
            return {'type': 'sensor', 'name': 'light'}
        elif str(arg_str).upper() == 'SENSOR_DISTANCIA':
            return {'type': 'sensor', 'name': 'distance'}
        
        try:
            if '.' in str(arg_str):
                return float(arg_str)
            return int(arg_str)
        except ValueError:
            return str(arg_str)

    def parse_comparison_string(comp_str):
        parts = re.split(r'\s+', comp_str.strip())
        
        if len(parts) == 4 and parts[0].upper() == "COMPARAR":
            left_operand = parse_arg_value(parts[1])
            operator = parts[2].upper()
            right_operand = parse_arg_value(parts[3])
            return {'type': 'comparison', 'left': left_operand, 'operator': operator, 'right': right_operand}
        else:
            raise ValueError(f"Formato de comparación inválido: '{comp_str}'. Se espera 'COMPARAR VALOR1 OPERADOR VALOR2'.")


    for i, (indentation, cmd, args) in enumerate(tokens):
        current_scope = scope_stack[-1]

        if cmd == "SI":
            if len(args) == 1:
                condition_str = args[0]
                condition = parse_comparison_string(condition_str)
                
                si_block = {'command': 'SI', 'condition': condition, 'body': []}
                current_scope.append(si_block)
                scope_stack.append(si_block['body'])
            else:
                raise ValueError(f"Error de sintaxis SI en línea {i+1}: {tokens[i]}. Se espera una única cadena de condición para el bloque SI (ej. 'COMPARAR VALOR1 OPERADOR VALOR2').")
        elif cmd == "FIN_SI":
            if len(scope_stack) <= 1:
                raise ValueError(f"Error de sintaxis en línea {i+1}: FIN_SI sin SI correspondiente.")
            scope_stack.pop()
        elif cmd == "REPETIR":
            if len(args) == 1:
                times = parse_arg_value(args[0])
                if not isinstance(times, int) or times < 0:
                    raise ValueError(f"El número de repeticiones debe ser un entero positivo en línea {i+1}: {tokens[i]}.")
                
                repetir_block = {'command': 'REPETIR', 'times': times, 'body': []}
                current_scope.append(repetir_block)
                scope_stack.append(repetir_block['body'])
            else:
                raise ValueError(f"Error de sintaxis REPETIR en línea {i+1}: {tokens[i]}. Se espera 'REPETIR <NUM> VECES'.")
        elif cmd == "FIN_REPETIR":
            if len(scope_stack) <= 1:
                raise ValueError(f"Error de sintaxis en línea {i+1}: FIN_REPETIR sin REPETIR correspondiente.")
            scope_stack.pop()
        elif cmd == "INICIAR":
            current_scope.append({'command': 'INICIAR'})
        elif cmd == "AVANZAR":
            if len(args) == 2:
                duration = parse_arg_value(args[0])
                speed = parse_arg_value(args[1])
                current_scope.append({'command': 'AVANZAR', 'duration': duration, 'speed': speed})
            else:
                raise ValueError(f"AVANZAR requiere 2 argumentos (duración, velocidad), se dieron {len(args)} en línea {i+1}.")
        elif cmd == "RETROCEDER":
            if len(args) == 2:
                duration = parse_arg_value(args[0])
                speed = parse_arg_value(args[1])
                current_scope.append({'command': 'RETROCEDER', 'duration': duration, 'speed': speed})
            else:
                raise ValueError(f"RETROCEDER requiere 2 argumentos (duración, velocidad), se dieron {len(args)} en línea {i+1}.")
        elif cmd == "GIRAR":
            if len(args) == 3:
                direction = str(args[0]).upper()
                speed = parse_arg_value(args[1])
                duration = parse_arg_value(args[2])
                current_scope.append({'command': 'GIRAR', 'direction': direction, 'speed': speed, 'duration': duration})
            else:
                raise ValueError(f"GIRAR (duración) requiere 3 argumentos (dirección, velocidad, duración), se dieron {len(args)} en línea {i+1}.")
        elif cmd == "GIRAR_ANGULO":
            if len(args) == 2:
                direction = str(args[0]).upper()
                angle = parse_arg_value(args[1])
                current_scope.append({'command': 'GIRAR_ANGULO', 'direction': direction, 'angle': angle})
            else:
                raise ValueError(f"GIRAR_ANGULO requiere 2 argumentos (dirección, ángulo), se dieron {len(args)} en línea {i+1}.")
        elif cmd == "ESPERAR":
            if len(args) == 1:
                duration = parse_arg_value(args[0])
                current_scope.append({'command': 'ESPERAR', 'duration': duration})
            else:
                raise ValueError(f"ESPERAR requiere 1 argumento (duración), se dieron {len(args)} en línea {i+1}.")
        elif cmd == "FINALIZAR":
            current_scope.append({'command': 'FINALIZAR'})
        elif cmd.startswith("SENSOR_") or re.match(r"^-?\d+(\.\d+)?$", cmd):
            raise ValueError(f"Valor o sensor '{cmd}' en línea {i+1} fuera de contexto. Debe ser parte de una comparación.")
        else:
            raise ValueError(f"Comando desconocido en línea {i+1}: {tokens[i]}.")

    if len(scope_stack) > 1:
        raise ValueError("Error de sintaxis: Bloques de control sin cerrar al final del programa.")

    return program_ast
