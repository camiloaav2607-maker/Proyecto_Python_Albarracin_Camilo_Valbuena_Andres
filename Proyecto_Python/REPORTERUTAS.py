
import json
import os

from TRAINERS import listar_trainers
from ALMACENAR import cargar_datos, guardar_datos



ARCHIVOr="reporte.json"

def estructura_inicial():
    
    return {
        
        "trainers": [listar_trainers]}



def cargar_datos(nombre_archivo=ARCHIVOr):
    
    if not os.path.exists(nombre_archivo):
        datos = estructura_inicial()
        guardar_datos(datos, nombre_archivo)
        return datos
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            datos = estructura_inicial()
            guardar_datos(datos, nombre_archivo)
            return datos

def guardar_datos(data, nombre_archivo=ARCHIVOr):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)









    
    
    
    
       





