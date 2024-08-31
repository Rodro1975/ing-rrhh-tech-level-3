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

## Características de la Página de Login

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

