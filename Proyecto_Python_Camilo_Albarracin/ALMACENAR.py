import json
import os

ARCHIVO = "data.json"

def estructura_inicial():
    return {
        "campers": [],
        "trainers": [],
        "rutas": [],
        "areas": [],
        "matriculas": [],
        "evaluaciones": []
    }

def cargar_datos(nombre_archivo=ARCHIVO):
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

def guardar_datos(data, nombre_archivo=ARCHIVO):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
