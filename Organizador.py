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
def Organizar(directorio):
    tipos_archivos= defaultdict(int)
    for ruta in directorio.iterdir():
        if ruta.is_dir():
            continue
        else:
            extension= ruta.suffix
            directorioext= directorio / extension
            directorioext.mkdir(parents=True,exist_ok=True)
            tipos_archivos[extension] += 1
            ruta.move_into(directorioext)
    return tipos_archivos
    

tipos = Organizar(directorio)
for extension, cantidad in tipos.items():
    print(f'Extension: {extension}, Cantidad: {cantidad}')

