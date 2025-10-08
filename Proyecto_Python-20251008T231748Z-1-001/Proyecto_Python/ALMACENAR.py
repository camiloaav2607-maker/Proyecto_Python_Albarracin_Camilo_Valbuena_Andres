import json
import os

ARCHIVO = "data.json"

def estructura_inicial():
    
    return {
        "campers": [],
        "trainers": [],
        "rutas": [
            {"nombre": "Fundamentos", "modulos": ["Lógica", "Python Básico"], "campers": []},
            {"nombre": "Backend", "modulos": ["Flask", "Bases de Datos"], "campers": []},
            {"nombre": "Frontend", "modulos": ["HTML", "CSS", "JavaScript"], "campers": []}
        ],
        "areas": [
            
            {"nombre": "Desarrollo Web", "capacidad": 33, "campers": []},
            {"nombre": "Desarrollo Movil", "capacidad": 33, "campers": []},
            {"nombre": "Desarrollo de Videojuegos", "capacidad": 33, "campers": []}
        ],
        "matriculas": [],
        "evaluaciones": [],
        "usuarios": [
            {"usuario": "admin", "clave": "1234", "rol": "coordinador"},
            {"usuario": "trainer1", "clave": "abcd", "rol": "trainer"},
            {"usuario": "camper1", "clave": "0000", "rol": "camper"}
        ]
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