import shutil
from pathlib import Path

print('===============================')
print('--- CLASIFICADOR DE ARCHIVOS ---')
print('===============================\n')
print('Este programa clasifica los archivos')
print('de la carpeta que le indiques dentro')
print('de carpetas por tipo de archivo\n')

# Recibe ruta absoluta o relativa
files_path = Path(input('Escribe la ruta:\n'))

file_types = []      # Lista con los tipos de archivos
folder_names = []    # Lista con los nombres de las carpetas creadas
folder_paths = []    # Lista de rutas de las carpetas
deleted_folders = [] # Lista de carpetas eliminadas

def find_type(path):  # Función que busca tipos de archivo

    for dir in path.iterdir():
        
        if dir.is_file():
            # Si el directorio es un archivo y su extensión no se
            # escuentra en la lista de tipos, la agrega
            if dir.suffix not in file_types:
                file_types.append(dir.suffix)
        
        # Si el directorio es una carpeta aplica la función de 
        # búsqueda de tipos    
        if dir.is_dir():
            find_type(dir)


def move_files(path):  # Función mover archivos
    
    for dir in path.iterdir():
        if dir.is_file():
            # Si el directorio es un archivo y y no se encuentra dentro de la
            # carpeta con su extensión se moverá a ella.
            # La carpeta se obtiene a partir el índice de la lista de tipos el
            # cual es el mismo para la carpeta de rutas de carpeta
            if not ((folder_paths[file_types.index(dir.suffix)]/dir.name).exists()):
                shutil.move(str(dir), str(folder_paths[file_types.index(dir.suffix)]))
        
        if dir.is_dir():
            # Si la ruta es una carpeta aplicará la función mover archivos
            move_files(dir)
            
            # Si la carpeta no se encuentra en la lista de las carpetas
            # de clasificación la eliminará y la agregará a la lista de 
            # las carpetas eliminadas.
            if not dir in folder_paths:
                deleted_folders.append(dir)
                dir.rmdir()

# Si la ruta escrita existe:
if files_path.exists():

    # Aplica la función búsqueda a la ruta definida por el usuario
    find_type(files_path)

    # Crea la lista de nombres de carpeta a partir de la lista de
    # tipos eliminando el punto y escribiéndolos en mayúscula
    # y en plural
    for type in file_types:
        folder_names.append(type[1:].upper()+'s')

    # Crea la lista de rutas de las carpetas a partir de sus
    # nombres    
    for name in folder_names:
        folder_paths.append(files_path/name)

    # Crea las carpetas a partir de su ruta si no existen aún
    for folder in folder_paths:
        if not folder.exists():
            folder.mkdir()


    # Aplica la función mover archivos a la ruta definida por el usuario
    move_files(files_path)

    # Imprime las carpetas creadas a partir de la lista de nombres
    print('\nLas carpetas creadas fueron:')
    for folder in folder_names:
        print(folder)

    # Imprime la ruta relativa de las carpetas eliminadas
    # respecto a la ruta definida por el usuario   
    print('\nLas carpetas eliminadas fueron:')
    for folder in deleted_folders:
        print(folder.relative_to(files_path))

# Si la ruta no existe manda un mensaje de error
else:
    print('\nERROR. La ruta introducida no existe')
