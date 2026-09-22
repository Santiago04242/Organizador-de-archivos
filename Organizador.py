import pathlib
import sys 
import os
from collections import defaultdict

#Manejo de error IndexError
try:
    carpeta= str(sys.argv[1])
except IndexError:
    carpeta= ''

#Fundion para obtener el directorio, si no se pasa ningun argumento se toma el directorio actual
def Obtener_directorio(carpeta):
    if carpeta=='.' or not carpeta:
        carpeta=os.getcwd()
    return pathlib.Path(carpeta)

#Se recorre el directorio y si encuentra un directorio continua, se extrae la extension del archivo y se crea una carpeta por cada tipo de extension
directorio= Obtener_directorio(carpeta)
def Organizar(directorio, is_preview=False):
    tipos_archivos= defaultdict(int)
    for ruta in directorio.iterdir():
        if ruta.is_dir():
            continue
        else:
            extension= ruta.suffix
            directorioext= directorio / extension
            tipos_archivos[extension] += 1
            if not is_preview:
                directorioext.mkdir(parents=True,exist_ok=True)
                ruta.move_into(directorioext)
    return tipos_archivos

def Desorganizar(directorio):
    for carpeta in directorio.iterdir():
        nombre_carpeta= carpeta.parents.name
        if carpeta.is_dir():
            for archivo in carpeta.iterdir():
                extension= archivo.suffix
                if extension==nombre_carpeta:
                    archivo.move_into(directorio)
        else:
            continue
    
#Se recorre el diccionario de tipos de archivos y se imprime la extension y la cantidad de archivos que tiene cada extension
tipos = Organizar(directorio, True)
for extension, cantidad in tipos.items():
    print(f'Extension: {extension}, Cantidad: {cantidad}')

