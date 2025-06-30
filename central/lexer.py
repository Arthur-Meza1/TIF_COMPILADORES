# lexer.py - Analizador léxico para los comandos de Blockly

import re

def lexer(text):
    """
    Toma un texto de comandos de Blockly y lo convierte en una lista de tokens.
    Cada token es una tupla: (indentación, comando_principal, [argumentos]).
    Maneja la indentación para estructuras de control y parsea condiciones complejas.
    """
    lines = text.strip().splitlines()
    tokens = []

    for line_num, line in enumerate(lines):
        # Ignorar líneas vacías
        if not line.strip():
            continue

        # Calcular la indentación
        stripped_line = line.lstrip()
        indentation = len(line) - len(stripped_line)
        parts = stripped_line.split()

        cmd = parts[0].upper()
        args = parts[1:]

        if cmd == "SI":
            try:
                entonces_idx = -1
                if "ENTONCES" in args:
                    entonces_idx = args.index("ENTONCES")
                elif "ENTÃO" in args:
                    entonces_idx = args.index("ENTÃO")
                
                if entonces_idx != -1:
                    condition_parts_raw = args[:entonces_idx]
                    
                    if len(condition_parts_raw) >= 4 and condition_parts_raw[0].upper() == "COMPARAR":
                        condition_str = " ".join(condition_parts_raw)
                        tokens.append((indentation, "SI", [condition_str]))
                    else:
                        raise ValueError(f"Condición de COMPARAR mal formada en línea {line_num + 1}: {line}")
                else:
                    raise ValueError(f"'ENTONCES' o 'ENTÃO' no encontrado en el bloque SI en línea {line_num + 1}.")
            except ValueError as e:
                raise ValueError(f"Error de sintaxis en SI en línea {line_num + 1}: {e.args[0] if e.args else 'Condición mal formada.'}")
        elif cmd == "FIN_SI":
            tokens.append((indentation, "FIN_SI", []))
        elif cmd == "REPETIR":
            if len(args) >= 2 and args[1].upper() == "VECES":
                num_veces = args[0].strip()
                tokens.append((indentation, "REPETIR", [num_veces]))
            else:
                raise ValueError(f"Formato incorrecto. Se espera 'REPETIR <NUM> VECES' en línea {line_num + 1}: {line}")
        elif cmd == "FIN_REPETIR":
            tokens.append((indentation, "FIN_REPETIR", []))
        elif cmd == "COMPARAR":
            raise ValueError(f"El comando 'COMPARAR' en línea {line_num + 1} debe estar anidado dentro de un SI.")
        elif cmd == "SENSOR_LUZ" or cmd == "SENSOR_DISTANCIA" or re.match(r"^-?\d+(\.\d+)?$", cmd):
            raise ValueError(f"Valor o sensor '{cmd}' en línea {line_num + 1} fuera de contexto. Debe ser parte de una expresión o comparación.")
        elif cmd in ["INICIAR", "AVANZAR", "RETROCEDER", "GIRAR", "GIRAR_ANGULO", "ESPERAR", "FINALIZAR"]:
            tokens.append((indentation, cmd, args))
        else:
            raise ValueError(f"Comando desconocido en línea {line_num + 1}: {line}.")
    return tokens
