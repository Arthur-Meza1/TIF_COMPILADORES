# main.py - Orquestador del compilador

from lexer import lexer
from parser import parser
from robot_controller import generar_codigo

def main():
    """
    Lee el archivo de entrada, lo tokeniza, lo parsea y genera el código Python final.
    """
    try:
        with open("entrada.txt", "r") as f:
            texto = f.read()

        tokens = lexer(texto)
        print("--- LEXER OUTPUT (TOKENS) ---")
        for i, token in enumerate(tokens):
            print(f"Token {i}: {token}")
        print("-----------------------------")

        comandos_ast = parser(tokens)
        print("\n--- PARSER OUTPUT (AST) ---")
        import json
        print(json.dumps(comandos_ast, indent=2))
        print("---------------------------\n")

        codigo_python_lines = generar_codigo(comandos_ast)
        codigo_python = "\n".join(codigo_python_lines)


        with open("controlador.py", "w") as f:
            f.write(codigo_python)

        print("\nArchivo 'controlador.py' generado exitosamente para usar en Webots.")
        print("Copia el contenido de controlador.py a tu controlador en Webots.")

    except FileNotFoundError:
        print("Error: 'entrada.txt' no encontrado. Asegúrate de que el archivo existe.")
    except ValueError as e:
        print(f"Error de compilación: {e}")
    except TypeError as e:
        print(f"Error de tipo: {e}. Esto podría significar que un tipo de dato inesperado fue recibido.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()
