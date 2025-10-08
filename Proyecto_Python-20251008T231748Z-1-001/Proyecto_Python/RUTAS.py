from ALMACENAR import cargar_datos, guardar_datos

def listar_rutas():
    data = cargar_datos()
    return data.get("rutas", [])

def asignar_camper_ruta(id_camper, nombre_ruta):
    data = cargar_datos()
    for ruta in data["rutas"]:
        if ruta["nombre"].lower() == nombre_ruta.lower():
            if id_camper not in ruta["campers"]:
                ruta["campers"].append(id_camper)
                guardar_datos(data)
                print("Camper asignado a la ruta")
                return
    raise ValueError("Ruta no encontrada.")
