from ALMACENAR import cargar_datos, guardar_datos
from CAMPERS import _find_camper 
from TRAINERS import encontrar_trainer 

def crear_matricula(id_camper, ruta, area, id_trainer, fecha_inicio, fecha_fin):
    data = cargar_datos()
    camper = _find_camper(data, id_camper)
    trainer = encontrar_trainer(data, id_trainer)

    
    if not camper:
        raise ValueError("Camper no encontrado.")
    if camper.get("estado") != "Aprobado":
        raise ValueError(f"El camper debe estar en estado 'Aprobado' para matricularse. Estado actual: {camper.get('estado')}")

    
    if not trainer:
        raise ValueError("Trainer no encontrado.")
    if ruta.lower() not in [r.lower() for r in trainer.get("rutas", [])]:
        raise ValueError(f"El Trainer {id_trainer} no está asignado a la ruta {ruta}.")

    
    
    
    matricula = {
        "id_camper": id_camper,
        "ruta": ruta,
        "area": area,
        "id_trainer": id_trainer, 
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin 
    }
    data["matriculas"].append(matricula)
    
    
    camper["estado"] = "Cursando"

    guardar_datos(data)
    print("Matricula creada y camper actualizado a 'Cursando'")

def listar_matriculas():
    data = cargar_datos()
    return data.get("matriculas", [])