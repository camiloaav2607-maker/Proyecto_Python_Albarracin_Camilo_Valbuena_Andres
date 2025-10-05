from ALMACENAR import cargar_datos, guardar_datos
from AREAS import validar_capacidad_area, asignar_camper_a_area

def crear_matricula(id_camper, id_trainer, ruta, fecha_inicio, fecha_fin, salon, area=None):
    data = cargar_datos()
    
    campers_ids = [c["id"] for c in data["campers"]]
    trainers_ids = [t["id"] for t in data["trainers"]]
    rutas_nombres = [r["nombre"] for r in data["rutas"]]

    if id_camper not in campers_ids:
        raise ValueError("Camper no registrado")
    if id_trainer not in trainers_ids:
        raise ValueError("Trainer no registrado")
    if ruta not in rutas_nombres:
        raise ValueError("Ruta no registrada")

    
    if area:
        if not validar_capacidad_area(area):
            raise ValueError("Area sin capacidad")
        asignar_camper_a_area(id_camper, area)

    matricula = {
        "id_camper": id_camper,
        "id_trainer": id_trainer,
        "ruta": ruta,
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "salon": salon
    }
    data["matriculas"].append(matricula)
    guardar_datos(data)

def crear_matricula_interactiva():
    id_camper = input("ID camper: ").strip()
    id_trainer = input("ID trainer: ").strip()
    ruta = input("Ruta: ").strip()
    fecha_inicio = input("Fecha inicio (YYYY-MM-DD): ").strip()
    fecha_fin = input("Fecha fin (YYYY-MM-DD): ").strip()
    salon = input("Salon: ").strip()
    area = input("Area (opcional): ").strip() or None
    crear_matricula(id_camper, id_trainer, ruta, fecha_inicio, fecha_fin, salon, area)
    print("Matrícula creada.")

def listar_matriculas():
    data = cargar_datos()
    return data["matriculas"]

def consultar_matricula_por_camper(id_camper):
    data = cargar_datos()
    return [m for m in data["matriculas"] if m["id_camper"] == id_camper]



