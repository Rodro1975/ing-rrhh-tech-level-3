# ing-rrhh-tech-level-3
Prueba técnica de selección L3

# Conteo de Colisiones

Este directorio contiene una solución para contar las colisiones entre robots dados en una secuencia de direcciones.

## Descripción del Problema

Dada una hilera de robots representada con las letras `R` (derecha) y `L` (izquierda), esta función determina cuántas veces colisiona cada robot bajo los siguientes supuestos:
- La distancia inicial entre robots es de 2 metros.
- Cuando dos robots chocan, cambian de dirección instantáneamente.
- El espacio es infinito en ambas direcciones.

## Ejecución

Para ejecutar el script colisiones.py, asegúrate de estar en el directorio colisiones. Usa los siguientes comandos:

cd colisiones
python colisiones.py

Para ejecutar las pruebas unitarias con unittest, asegúrate de que el archivo test_colisiones.py esté en el mismo directorio desde donde estás ejecutando el comando, o usa la ruta relativa. Navega al directorio colisiones y ejecuta:

python -m unittest test_colisiones

## Ejemplos de Uso

- Ejecutar el script: Proporciona ejemplos de cómo debe lucir la entrada y cuál será la salida esperada.
### Entrada:
python colisiones.py
### Salida esperada: 

0 0
1 1
0 0 0
1 2 1

- Ejecutar pruebas unitarias: Explica brevemente qué tipos de pruebas se están realizando.
### Entrada:
  python -m unittest test_colisiones
### Salida esperada:

0 0
1 1
0 0 0
1 2 1.

Ran 1 test in 0.002s

OK

## Requisitos
Asegúrate de tener Python 3.12.4 instalado en tu sistema. No se requieren dependencias adicionales.

## Errores Comunes
Si ves errores como ModuleNotFoundError, verifica que el archivo test_colisiones.py esté en el directorio correcto y que el nombre del archivo sea correcto.

# Características de la Página de Login

- **Username y Password:** Campos de entrada para el nombre de usuario y la contraseña.
- **Remember me:** Una casilla de verificación para recordar al usuario.
- **Forgot your password?:** Un enlace para recuperar la contraseña olvidada.
- **Diseño Responsivo:** Utiliza CSS3 para hacer que la página sea responsiva en diferentes dispositivos.

### Archivos en la Carpeta `login`

- **index.html:** El archivo principal HTML que estructura la página de login.
- **styles.css:** El archivo CSS que contiene los estilos para la página.
- **images/**: Carpeta que contiene las imágenes necesarias para el diseño, como el logo de la compañía.

### Cómo Ejecutar

Para visualizar la página de login, simplemente abre `index.html` en un navegador web.

----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------

# ing-rrhh-tech-level-3
# L3 technical selection test

## Collision Count
This directory contains a solution to count collisions between given robots in a sequence of addresses.

## Problem Description
Given a row of robots represented by the letters R (right) and L (left), this function determines how many times each robot collides under the following assumptions:

The initial distance between robots is 2 meters.
When two robots collide, they change direction instantly.
Space is infinite in both directions.
## Execution
To run the collisions.py script, make sure you are in the collisions directory. Use the following commands:

cd collisions python collisions.py

To run unit tests with unittest, make sure the test_collisions.py file is in the same directory where you are running the command from, or use the relative path. Navigate to the collisions directory and run:

python -m unittest test_collisions

## Examples of Use
Run the script: Provides examples of what the input should look like and what the expected output will be.
## Entrance:
python collisions.py

## Expected output:
0 0 1 1 0 0 0 1 2 1

Run unit tests: Briefly explain what types of tests are being performed.
## Entrance:
python -m unittest test_collisions

## Expected output:
0 0 1 1 0 0 0 1 2 1.

Ran 1 test in 0.002s

OK

## Requirements
Make sure you have Python 3.12.4 installed on your system. No additional dependencies required.

## Common Errors
If you see errors like ModuleNotFoundError, check that the test_collisions.py file is in the correct directory and that the file name is correct.

# Login Page Features
- **Username and Password:** Entry fields for the username and password.
- **Remember me:** A checkbox to remember the user.
- **Forgot your password?:** A link to recover your forgotten password.
- **Responsive Design:** Use CSS3 to make the page responsive on different devices.
## Files in the login Folder
index.html: The main HTML file that structures the login page.
styles.css: The CSS file that contains the styles for the page.
images/: Folder that contains the images necessary for the design, such as the company logo.
## How to Run
To view the login page, simply open index.html in a web browser.

