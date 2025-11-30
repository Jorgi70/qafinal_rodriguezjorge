import csv
import pathlib

def leer_csv(ruta_archivo):
    datos = []
    ruta = pathlib.Path(ruta_archivo)
    with open(ruta, newline='',encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            debe_funcionar = fila['debe_funcionar'].lower() == 'true'
            datos.append((fila['usuario'], fila['password'],debe_funcionar))
            
    return datos 

print(leer_csv("datos/data_login.csv"))