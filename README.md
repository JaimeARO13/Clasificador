# CLASIFICADOR

- Este programa permite clasificar los archivos contenidos en un directorio dentro de carpetas que agrupan tales archivos por su extensión.

## Instrucciones

- El usuario ejecutará el archivo con el comando `python3 sorter.py` en la terminal.
- El programa pide al usuario que introduzca la ruta de la carpeta que desea clasificar.
- El programa recibe la ruta absoluta o relativa de la carpeta a ordenar, por ejemplo.
  - `C:\Users\Usuario\Documents/Archivos`
  - `Documents/Archivos`
- Si la ruta no existe el programa envía un mensaje de error.
- Si la ruta es valida, el programa crea una carpeta con el nombre en plural para cada extensión de archivo que detecte en la carpeta y subcarpetas.
- Los archivos son movidos a la carpeta correspondiente.
- Finalmente muestra las carpetas que fueron creadas y aquellas que fueron eliminadas.

