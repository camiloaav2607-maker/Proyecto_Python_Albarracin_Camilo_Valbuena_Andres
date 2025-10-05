from ALMACENAR import cargar_datos, guardar_datos

def _find_ruta(data, nombre_ruta):
    for r in data["rutas"]:
        if r["nombre"].lower() == nombre_ruta.lower():
            return r
    return None

def crear_ruta(nombre, modulos, sgdb_principal=None, sgdb_alternativo=None):
    data = cargar_datos()
    if _find_ruta(data, nombre):
        raise ValueError("La ruta ya existe")
    ruta = {
        "nombre": nombre,
        "modulos": modulos,
        "sgdb_principal": sgdb_principal,
        "sgdb_alternativo": sgdb_alternativo,
        "campers": []
    }
    data["rutas"].append(ruta)
    guardar_datos(data)

def crear_ruta_interactiva():
    nombre = input("Nombre ruta: ").strip()
    print("Ingrese los módulos separados por coma:")
    modulos = [m.strip() for m in input().split(",") if m.strip()]
    sgdb_prin = input("SGDB principal (opcional): ").strip() or None
    sgdb_alt = input("SGDB alternativo (opcional): ").strip() or None
    crear_ruta(nombre, modulos, sgdb_prin, sgdb_alt)
    print("Ruta creada")

def listar_rutas():
    data = cargar_datos()
    return data["rutas"]

def asignar_camper_a_ruta(id_camper, nombre_ruta):
    data = cargar_datos()
    ruta = _find_ruta(data, nombre_ruta)
    if not ruta:
        raise ValueError("Ruta no encontrada")
    if id_camper in ruta["campers"]:
        return
    ruta["campers"].append(id_camper)
    guardar_datos(data)



