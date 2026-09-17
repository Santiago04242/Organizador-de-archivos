import pathlib
import sys 
import os

#Manejo de error IndexError
try:
    carpeta= str(sys.argv[1])
except IndexError:
    carpeta= ''

#Si no se le pasa carpeta usa cwd (current working directory)
if carpeta=='.' or not carpeta:
    carpeta=os.getcwd()
directorio= pathlib.Path(carpeta)

#Se recorre el directorio y si encuentra un directorio continua, se extrae la extension del archivo y se crea una carpeta por cada tipo de extension
for ruta in directorio.iterdir():
    if ruta.is_dir():
        continue
    else:
        extension= ruta.suffix
        directorioext= directorio / extension
        directorioext.mkdir(parents=True,exist_ok=True)
        ruta.move_into(directorioext)

print('Organizado correctamente')

