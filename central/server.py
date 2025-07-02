# server.py - Servidor local para automatizar la compilación de Blockly a Webots

from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Asegúrate de que los módulos de tu compilador estén en el PATH.
# Si main.py, lexer.py, parser.py, robot_controller.py están en la misma carpeta que server.py,
# no necesitarás añadir nada especial aquí, pero si están en una subcarpeta, ajústalo.
# sys.path.append(os.path.dirname(os.path.abspath(__file__))) # Descomentar si los archivos están en una subcarpeta diferente

# Importa la función de compilación de main.py
try:
    import main
except ImportError:
    print("Error: No se pudo importar 'main.py'. Asegúrate de que está en la misma carpeta que server.py.")
    sys.exit(1)


app = Flask(__name__)
CORS(app) # Habilita CORS para permitir que tu HTML haga solicitudes desde el navegador

# WEBOTS_CONTROLLER_PATH = "C:\\Users\\TuUsuario\\WebotsProjects\\MiProyectoRobot\\controllers\\my_robot_controller\\my_robot_controller.py" # Windows
# WEBOTS_CONTROLLER_PATH = "/home/TuUsuario/WebotsProjects/MiProyectoRobot/controllers/my_robot_controller/my_robot_controller.py" # Linux/macOS
WEBOTS_CONTROLLER_PATH = "C:\\Users\\porot\\Compiladores\\controllers\\my_robot_controller\\my_robot_controller.py" # ¡CAMBIA ESTO!
# ----------------------------------------------------

@app.route('/save_and_compile', methods=['POST'])
def save_and_compile():
    """
    Recibe el código de Blockly, lo guarda en entrada.txt,
    y luego ejecuta el proceso de compilación.
    """
    data = request.get_json()
    blockly_code = data.get('code')

    if not blockly_code:
        return jsonify({"status": "error", "message": "No se recibió código de Blockly."}), 400

    try:
        # 1. Guardar el código de Blockly en entrada.txt
        with open("entrada.txt", "w") as f:
            f.write(blockly_code)
        print("Código de Blockly guardado en entrada.txt")

        # 2. Ejecutar la lógica de compilación de main.py
        # Pasamos la ruta del controlador de Webots a la función de compilación
        compilation_success, compilation_message = main.run_compilation(WEBOTS_CONTROLLER_PATH)

        if compilation_success:
            return jsonify({"status": "success", "message": "Código guardado y compilado exitosamente. " + compilation_message}), 200
        else:
            return jsonify({"status": "error", "message": "Error durante la compilación: " + compilation_message}), 500

    except Exception as e:
        print(f"Error en el servidor: {e}")
        return jsonify({"status": "error", "message": f"Error interno del servidor: {str(e)}"}), 500

@app.route('/')
def index():
    return "Servidor de compilación de Blockly para Webots. Accede a la interfaz Blockly en tu navegador."

if __name__ == '__main__':
    # Verifica si la ruta del controlador de Webots ha sido configurada
    if WEBOTS_CONTROLLER_PATH == "RUTA_ABSOLUTA_A_TU_CONTROLADOR_EN_WEBOTS.py":
        print("\n¡ADVERTENCIA! La variable 'WEBOTS_CONTROLLER_PATH' en server.py NO ha sido configurada.")
        print("El archivo 'controlador.py' se generará en la misma carpeta que main.py (para pruebas).")
        print("Para una automatización completa, por favor, edita 'server.py' y establece la ruta correcta.")
        # Usamos una ruta temporal para que el servidor pueda arrancar y main.py siga funcionando.
        WEBOTS_CONTROLLER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "controlador_temp.py")


    print(f"\n--- Servidor Flask Iniciado ---")
    print(f"Asegúrate de que tus archivos lexer.py, parser.py, robot_controller.py y main.py")
    print(f"estén en la misma carpeta que server.py.")
    print(f"Abre tu archivo HTML de Blockly en el navegador (ej. file:///ruta/a/tu/blockly_robot.html).")
    print(f"El controlador de Webots se escribirá en: {WEBOTS_CONTROLLER_PATH}")
    print(f"-------------------------------\n")
    app.run(debug=True) # debug=True para desarrollo, deshabilitar en producción
