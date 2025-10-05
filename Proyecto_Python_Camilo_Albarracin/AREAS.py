from ALMACENAR import cargar_datos, guardar_datos

DEFAULT_CAPACIDAD = 33

def _find_area(data, nombre_area):
    for a in data["areas"]:
        if a["nombre"].lower() == nombre_area.lower():
            return a
    return None

def crear_area(nombre, capacidad=DEFAULT_CAPACIDAD):
    data = cargar_datos()
    if _find_area(data, nombre):
        raise ValueError("El area ya existe")
    area = {"nombre": nombre, "capacidad": capacidad, "campers": []}
    data["areas"].append(area)
    guardar_datos(data)

def crear_area_interactiva():
    nombre = input("Nombre del area: ").strip()
    capacidad = input(f"Capacidad (por defecto {DEFAULT_CAPACIDAD}): ").strip()
    capacidad = int(capacidad) if capacidad.isdigit() else DEFAULT_CAPACIDAD
    crear_area(nombre, capacidad)
    print("Area creada.")

def listar_areas():
    data = cargar_datos()
    return data["areas"]

def validar_capacidad_area(nombre_area):
    data = cargar_datos()
    area = _find_area(data, nombre_area)
    if not area:
        raise ValueError("Area no encontrada")
    return len(area["campers"]) < area["capacidad"]

def asignar_camper_a_area(id_camper, nombre_area):
    data = cargar_datos()
    area = _find_area(data, nombre_area)
    if not area:
        raise ValueError("Area no encontrada")
    if not validar_capacidad_area(nombre_area):
        raise ValueError("Area sin capacidad disponible")
    if id_camper in area["campers"]:
        return
    area["campers"].append(id_camper)
    guardar_datos(data)

    
