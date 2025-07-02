Herramienta Educativa de Programación Visual para el Robot e-puck en Webots con Blockly
Este proyecto proporciona un sistema intuitivo y automatizado para programar un robot e-puck en el simulador Webots, utilizando una interfaz visual de programación basada en bloques (Blockly). Diseñado pensando en la facilidad de uso, permite a usuarios sin experiencia en programación generar código Python complejo para controlar el robot con simples acciones de arrastrar y soltar.

 Características Principales
Interfaz Visual de Blockly: Un entorno de programación amigable donde puedes construir la lógica del robot arrastrando y conectando bloques.

Bloques Personalizados para e-puck: Bloques específicos para movimientos (avanzar, retroceder, girar por ángulo o tiempo), control (condicionales SI, bucles REPETIR) y sensores (luz, distancia).

Unidades Intuitivas: Los movimientos de avance/retroceso y espera se definen en segundos, y los giros en grados, haciendo la programación más natural para principiantes.

Compilador Personalizado: Un backend en Python que traduce los programas de Blockly a código Python ejecutable por el controlador de Webots.

Automatización Completa: Un servidor Flask local que permite que la interfaz de Blockly envíe el código directamente al compilador, el cual luego escribe el archivo .py del controlador de Webots de forma automática. ¡Olvídate de copiar y pegar en la terminal!

Depuración Mejorada: Mensajes de consola detallados en cada etapa del proceso (lexer, parser, generación de código) para facilitar la depuración.

 Estructura del Proyecto
Central/
├── venv/                     # Entorno virtual de Python
├── server.py                 # Servidor Flask que orquesta la automatización
├── main.py                   # Orquestador del compilador (llamado por server.py)
├── lexer.py                  # Analizador léxico: convierte texto de Blockly en tokens
├── parser.py                 # Analizador sintáctico: construye el AST a partir de tokens
├── robot_controller.py       # Generador de código Python para Webots
└── entrada.txt               # Archivo temporal donde Blockly guarda el código (se sobrescribe automáticamente)

blockly interface/   # Esta carpeta puede estar en cualquier lugar
├── index.html
├──custom_blocks.js      
└── generator.js
webots necesario/ # Carpeta contiene webots solo para linux         
 Requisitos Previos
Antes de comenzar, asegúrate de tener instalado lo siguiente en tu sistema operativo (Linux ) sino puedes descargar de la pagina oficial 

Python 3.x: Preferiblemente Python 3.8 o superior.

pip: El gestor de paquetes de Python (suele venir con Python).

Webots: El simulador de robots (descárgalo desde https://cyberbotics.com/).

Flask y Flask-CORS: Librerías de Python para el servidor web.

 Configuración e Instalación
Sigue estos pasos para poner en marcha el proyecto:

Clonar el Repositorio:

git clone https://github.com/[TU_USUARIO_GITHUB]/[NOMBRE_DE_TU_REPOSITORIO].git
cd [NOMBRE_DE_TU_REPOSITORIO]

(Ajusta [NOMBRE_DE_TU_REPOSITORIO] si has usado una estructura diferente como central.)

Organizar Archivos (si es necesario):
Asegúrate de que todos los archivos .py (server.py, main.py, lexer.py, parser.py, robot_controller.py) y el archivo entrada.txt estén en la misma carpeta (ej. tu_proyecto_robot_backend/). El blockly_robot.html puede estar en una carpeta separada (ej. tu_proyecto_robot_frontend/).

Crear y Activar el Entorno Virtual:
Navega a la carpeta que contiene todos tus archivos Python (ej. tu_proyecto_robot_backend/).

cd /ruta/a/tu/carpeta/principal/python # Ej: cd ~/Documentos/mi_proyecto_robot_backend
python -m venv venv
source venv/bin/activate

(Verás (venv) al inicio de tu línea de comandos si el entorno se activó correctamente.)

Instalar Dependencias de Python:
Con el entorno virtual activo, instala Flask y Flask-CORS:

pip install Flask Flask-CORS

⚠️ Configurar la Ruta del Controlador de Webots:
Abre el archivo server.py en tu editor de texto. Busca la línea:

WEBOTS_CONTROLLER_PATH = "RUTA_ABSOLUTA_A_TU_CONTROLADOR_EN_WEBOTS.py" # ¡CAMBIA ESTO!

Reemplaza "RUTA_ABSOLUTA_A_TU_CONTROLADOR_EN_WEBOTS.py" con la ruta completa y exacta al archivo .py de tu controlador de robot en tu proyecto de Webots.

Ejemplo (Windows): "C:\\Users\\TuUsuario\\WebotsProjects\\MiProyectoRobot\\controllers\\my_robot_controller\\my_robot_controller.py"

Ejemplo (Linux/macOS): "/home/TuUsuario/WebotsProjects/MiProyectoRobot/controllers/my_robot_controller/my_robot_controller.py"

¡Asegúrate de que el nombre del archivo .py coincida con el nombre de la carpeta del controlador en Webots!

🏃 Flujo de Uso (El Recorrido Automatizado)
Una vez que todo esté configurado, el proceso para programar tu robot es el siguiente:

Iniciar el Servidor Local:
Abre tu terminal. Navega a la carpeta principal de tus archivos Python (ej. tu_proyecto_robot_backend/).
Con el entorno virtual activo (source venv/bin/activate), ejecuta:

python server.py

Mantén esta terminal abierta y el servidor corriendo mientras uses Blockly.

Abrir la Interfaz de Blockly:
En tu navegador web, abre el archivo blockly_robot.html. Puedes arrastrar el archivo directamente al navegador o navegar a su ubicación.

Diseñar tu Programa en Blockly:
En el área de trabajo de Blockly, verás un programa de ejemplo precargado. Puedes modificarlo o crear uno nuevo arrastrando y conectando los bloques disponibles en el menú lateral.

Automatizar la Compilación y Generación del Controlador:
Cuando tu programa de bloques esté listo, haz clic en el botón "Automatizar Todo" en la interfaz de Blockly.

Verás un mensaje de estado en la página de Blockly (ej. "Código guardado y compilado exitosamente...").

En la terminal donde corre server.py, verás los mensajes de la compilación (lexer, parser, etc.).

En este punto, el archivo .py de tu controlador de Webots ya ha sido actualizado automáticamente.

Actualizar y Ejecutar en Webots:
Ve a tu simulación de Webots. Para que Webots cargue el código recién generado, necesitas reiniciar la simulación. Puedes hacerlo de varias maneras:

Presionando Ctrl + R (o Cmd + R en Mac).

Haciendo clic en el botón de "Reiniciar" o "Reload" en la interfaz de Webots (suele ser un icono de flechas circulares).

¡Tu robot ahora ejecutará el nuevo programa que diseñaste en Blockly!

 Ejemplo de Programa Precargado
Al abrir blockly_robot.html, verás un programa de ejemplo que hace lo siguiente:

Avanza 1 segundo a velocidad 3.

Repite 3 veces:

Si el sensor de distancia frontal detecta un valor mayor a 500 (indicando un obstáculo cercano):

Gira 90 grados a la izquierda.

Avanza 1.5 segundos a velocidad 1.

Si no hay obstáculo (o después de girar y avanzar):

Retrocede 0.7 segundos a velocidad 2.

Espera 0.2 segundos.

Finaliza el programa.

Este ejemplo te sirve como punto de partida para experimentar con los bloques.

 Resolución de Problemas Comunes
externally-managed-environment al instalar Flask: Esto significa que tu entorno virtual no estaba activo. Asegúrate de ejecutar source venv/bin/activate antes de pip install Flask Flask-CORS.

bash: venv/bin/activate: No existe el fichero o el directorio: Asegúrate de que estás en la carpeta que contiene la carpeta venv cuando ejecutas source venv/bin/activate.

"Error de conexión con el servidor" en Blockly: Asegúrate de que server.py está corriendo en tu terminal y no hay errores en su inicio. También verifica que la URL http://127.0.0.1:5000 no esté siendo bloqueada por un firewall.

El robot no hace nada en Webots:

Verifica que server.py no haya reportado errores de compilación.

Asegúrate de haber configurado correctamente WEBOTS_CONTROLLER_PATH en server.py.

¡Siempre reinicia la simulación en Webots después de cada cambio! Webots no carga automáticamente el nuevo código.

Verifica los nombres de los sensores en robot_controller.py (ps7, ls6) para que coincidan con los de tu modelo de e-puck en Webots.
