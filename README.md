🤖 Herramienta Educativa de Programación Visual para el Robot e-puck en Webots
Este proyecto ofrece un sistema innovador y automatizado para controlar el robot e-puck dentro del simulador Webots, utilizando una interfaz de programación visual basada en bloques (Blockly). Ha sido diseñado pensando en la facilidad de uso, permitiendo a usuarios de todos los niveles, incluso sin experiencia previa en programación, generar código Python complejo para el robot mediante simples acciones de arrastrar y soltar.

✨ Características Destacadas
Interfaz Visual Intuitiva (Blockly): Un entorno de programación amigable que facilita la construcción de la lógica del robot mediante bloques visuales.

Bloques Personalizados para e-puck: Incluye bloques específicos para controlar movimientos (avanzar, retroceder, girar por ángulo o tiempo), estructuras de control (condicionales SI, bucles REPETIR) y la lectura de sensores (luz, distancia).

Unidades de Medida Naturales: Los movimientos de avance/retroceso y las pausas se definitan en segundos, y los giros en grados, lo que hace la programación más intuitiva y cercana al lenguaje natural.

Compilador Personalizado en Python: Un potente backend desarrollado en Python que se encarga de traducir los programas creados en Blockly a código Python ejecutable, listo para ser interpretado por el controlador del robot en Webots.

Automatización Completa del Flujo de Trabajo: Incorpora un servidor Flask local que permite que la interfaz de Blockly envíe el código generado directamente al compilador. Este, a su vez, escribe el archivo .py del controlador de Webots de forma totalmente automática, eliminando la necesidad de copiar y pegar comandos en la terminal.

Depuración Asistida: Proporciona mensajes detallados en la consola durante cada etapa del proceso de compilación (análisis léxico, análisis sintáctico, generación de código), lo que facilita enormemente la identificación y resolución de posibles problemas.

📁 Estructura del Proyecto
La organización del proyecto se divide en módulos claros para una mejor gestión y comprensión:

Central/
├── venv/                     # Entorno virtual de Python para el aislamiento de dependencias.
├── server.py                 # Servidor Flask que actúa como puente entre Blockly y el compilador.
├── main.py                   # Orquestador principal del proceso de compilación.
├── lexer.py                  # Componente encargado del análisis léxico del código de Blockly.
├── parser.py                 # Componente encargado del análisis sintáctico (construcción del AST).
├── robot_controller.py       # Generador de código Python específico para el controlador de Webots.
└── entrada.txt               # Archivo temporal donde se almacena el código de Blockly antes de la compilación.

blockly interface/            # Contiene los archivos de la interfaz de usuario de Blockly.
├── index.html                # La página principal de la interfaz Blockly.
├── custom_blocks.js          # Definiciones de bloques personalizados de Blockly.
└── generator.js              # Lógica para generar código a partir de los bloques de Blockly.

webots necesario/             # Carpeta con recursos específicos para Webots (ej. modelos, controladores base).
└── # (archivos de Webots, ej. controladores por defecto, modelos de mundo)

⚙️ Requisitos Previos
Para asegurar el correcto funcionamiento de este proyecto, es necesario tener instalados los siguientes componentes en tu sistema operativo (preferiblemente Linux):

Python 3.x: Se recomienda Python 3.8 o una versión superior.

pip: El gestor de paquetes estándar de Python (generalmente incluido con la instalación de Python).

Webots: El simulador de robots, disponible para descarga en https://cyberbotics.com/.

Librerías Python:

Flask: Para la creación del servidor web local.

Flask-CORS: Para gestionar las políticas de seguridad de origen cruzado en el navegador.

🚀 Configuración e Instalación Paso a Paso
Sigue estas instrucciones detalladas para preparar y ejecutar el proyecto en tu entorno:

Clonar el Repositorio:
Abre tu terminal y clona este repositorio de GitHub. Sustituye [TU_USUARIO_GITHUB] y [NOMBRE_DE_TU_REPOSITORIO] por tus datos reales.

git clone https://github.com/[TU_USUARIO_GITHUB]/[NOMBRE_DE_TU_REPOSITORIO].git
cd [NOMBRE_DE_TU_REPOSITORIO]

(Si tu estructura de carpetas difiere, por ejemplo, si Central/ es la raíz de tu repositorio, ajusta el comando cd en consecuencia.)

Organizar Archivos (Verificación):
Asegúrate de que todos los archivos Python (server.py, main.py, lexer.py, parser.py, robot_controller.py) y el archivo entrada.txt se encuentren en la carpeta Central/. La carpeta blockly interface/ con index.html, custom_blocks.js y generator.js puede estar en cualquier otra ubicación conveniente.

Crear y Activar el Entorno Virtual:
Navega a la carpeta Central/ (donde se encuentran tus archivos Python).

cd /ruta/a/tu/carpeta/Central # Ej: cd ~/Documentos/Compi_TID/Central
python -m venv venv
source venv/bin/activate

(La aparición de (venv) al inicio de tu línea de comandos confirma que el entorno virtual está activo.)

Instalar Dependencias de Python:
Con el entorno virtual activo, instala las librerías necesarias:

pip install Flask Flask-CORS

⚠️ Configurar la Ruta del Controlador de Webots (CRÍTICO):
Abre el archivo server.py en tu editor de código. Localiza la variable WEBOTS_CONTROLLER_PATH:

WEBOTS_CONTROLLER_PATH = "RUTA_ABSOLUTA_A_TU_CONTROLADOR_EN_WEBOTS.py" # ¡CAMBIA ESTO!

Es fundamental que reemplaces "RUTA_ABSOLUTA_A_TU_CONTROLADOR_EN_WEBOTS.py" con la ruta completa y exacta al archivo .py de tu controlador de robot dentro de tu proyecto de Webots.

Ejemplo (Windows): "C:\\Users\\TuUsuario\\WebotsProjects\\MiProyectoRobot\\controllers\\my_robot_controller\\my_robot_controller.py"

Ejemplo (Linux/macOS): "/home/arthurm/Documentos/Compi_TID/webots_necesario/controllers/my_controller/my_controller.py"

¡Asegúrate de que el nombre del archivo .py (ej. my_controller.py) coincida con el nombre de la carpeta que lo contiene en Webots (ej. my_controller)!

🏃 Flujo de Uso (El Recorrido Automatizado)
Una vez que todos los componentes estén configurados y listos, el proceso para programar y probar tu robot es sorprendentemente sencillo:

Iniciar el Servidor Local:
Abre una terminal. Navega a la carpeta Central/ (donde están tus archivos Python). Con el entorno virtual activo (source venv/bin/activate), ejecuta el servidor:

python server.py

Mantén esta terminal abierta y el servidor en ejecución durante todo el proceso de programación y prueba.

Abrir la Interfaz de Blockly:
En tu navegador web, abre el archivo index.html que se encuentra en la carpeta blockly interface/. Puedes arrastrar el archivo directamente a la ventana del navegador o usar la opción "Abrir archivo..." de tu navegador.

Diseñar tu Programa en Blockly:
En el área de trabajo de Blockly, encontrarás un programa de ejemplo precargado que puedes explorar o modificar. Utiliza los bloques disponibles en el menú lateral para construir la lógica que desees para tu robot.

Automatizar la Compilación y Actualización del Controlador:
Una vez que tu programa de bloques esté completo, haz clic en el botón "Automatizar Todo" en la interfaz de Blockly.

Verás un mensaje de estado en la propia página de Blockly (ej. "Código guardado y compilado exitosamente...").

En la terminal donde se ejecuta server.py, podrás observar los mensajes detallados de las etapas de compilación (análisis léxico, sintáctico, generación de código).

En este momento, el archivo .py de tu controlador de Webots ya ha sido actualizado automáticamente con el nuevo código generado.

Actualizar y Ejecutar en Webots:
Dirígete al simulador Webots. Para que el robot cargue y ejecute el código recién generado, es necesario reiniciar la simulación. Puedes hacerlo de varias maneras:

Presionando la combinación de teclas Ctrl + R (o Cmd + R en macOS).

Haciendo clic en el botón de "Reiniciar" o "Reload" (generalmente un icono de flechas circulares) en la interfaz de Webots.

¡Observa cómo tu robot e-puck cobra vida y ejecuta el programa que diseñaste visualmente en Blockly!

💡 Ejemplo de Programa Precargado
Al abrir index.html, la interfaz de Blockly mostrará automáticamente un programa de ejemplo que ilustra las capacidades del sistema:

El robot avanza durante 1 segundo a una velocidad de 3.

Luego, repite el siguiente bloque de acciones 3 veces:

Condicional SI: Si el sensor de distancia frontal detecta un valor mayor a 500 (lo que podría indicar un obstáculo cercano):

El robot gira 90 grados a la izquierda.

Inmediatamente después, avanza 1.5 segundos a una velocidad de 1.

Acciones Post-Condicional: (Estas se ejecutan si la condición SI no se cumple, o después de que se ejecuten las acciones dentro del SI):

El robot retrocede 0.7 segundos a una velocidad de 2.

Finalmente, espera durante 0.2 segundos antes de la siguiente iteración del bucle.

El programa finaliza.

Este ejemplo sirve como un excelente punto de partida para que los usuarios experimenten y comprendan cómo interactúan los diferentes bloques.

🐛 Resolución de Problemas Comunes
Si encuentras algún inconveniente durante la configuración o el uso, consulta esta sección para encontrar soluciones:

externally-managed-environment al instalar Flask: Este error indica que tu entorno virtual no estaba activo al intentar instalar paquetes. Asegúrate de ejecutar source venv/bin/activate antes de pip install Flask Flask-CORS.

bash: venv/bin/activate: No existe el fichero o el directorio: Verifica que estás en la carpeta que contiene la carpeta venv cuando ejecutas source venv/bin/activate. Confirma la existencia de la carpeta venv y su contenido (venv/bin/activate).

"Error de conexión con el servidor" en Blockly: Asegúrate de que server.py esté corriendo en tu terminal y que no haya mostrado ningún error al iniciarse. Verifica también que la URL http://127.0.0.1:5000 no esté siendo bloqueada por un firewall o antivirus en tu sistema.

El robot no se mueve o no responde en Webots:

Revisa la terminal donde se ejecuta server.py para verificar si hubo errores de compilación reportados.

Confirma que la variable WEBOTS_CONTROLLER_PATH en server.py esté configurada con la ruta absoluta y correcta a tu archivo .py del controlador de Webots.

¡Es crucial reiniciar la simulación en Webots (Ctrl + R o Cmd + R) después de cada cambio en el código del controlador! Webots no recarga el código automáticamente.

Verifica que los nombres de los sensores utilizados en robot_controller.py (ej. 'ps7', 'ls6') coincidan exactamente con los nombres de los nodos de los sensores en tu modelo de e-puck en Webots.

🤝 Contribución
¡Tu colaboración es muy valorada! Si tienes ideas para mejorar los bloques existentes, desarrollar nuevos, optimizar el compilador o la interfaz de usuario, no dudes en abrir un "issue" para discutirlo o enviar un "pull request" con tus propuestas.

📄 Licencia
Este proyecto se distribuye bajo la licencia [Tipo de Licencia, ej. MIT License]. Consulta el archivo LICENSE en el repositorio para obtener más detalles.
