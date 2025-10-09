from ALMACENAR import cargar_datos, guardar_datos

def listar_areas():
    data = cargar_datos()
    return data.get("areas", [])

def validar_capacidad_area(area):
    return len(area.get("campers", [])) < area.get("capacidad", 0)

def asignar_camper_area(id_camper, nombre_area):
    data = cargar_datos()
    for a in data["areas"]:
        if a["nombre"].lower() == nombre_area.lower():
            if not validar_capacidad_area(a):
                raise ValueError("Área sin capacidad disponible.")
            if id_camper not in a["campers"]:
                a["campers"].append(id_camper)
                guardar_datos(data)
                print("Camper asignado al area")
                return
    raise ValueError("Área no encontrada.")