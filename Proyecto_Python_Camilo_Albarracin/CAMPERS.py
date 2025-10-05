from ALMACENAR import cargar_datos, guardar_datos

VALID_ESTADOS = [
    "En proceso de ingreso", "Inscrito", "Aprobado",
    "Cursando", "Graduado", "Expulsado", "Retirado"
]

def _find_camper(data, id_camper):
    for c in data["campers"]:
        if c["id"] == id_camper:
            return c
    return None

def registrar_camper(camper):
    data = cargar_datos()
    if _find_camper(data, camper["id"]):
        raise ValueError(f"Ya existe un camper con id {camper['id']}")
    data["campers"].append(camper)
    guardar_datos(data)

def registrar_camper_interactivo():
    camper = {
        "id": input("ID: ").strip(),
        "nombres": input("Nombres: ").strip(),
        "apellidos": input("Apellidos: ").strip(),
        "direccion": input("Dirección: ").strip(),
        "acudiente": input("Acudiente: ").strip(),
        "telefono_celular": input("Teléfono celular: ").strip(),
        "telefono_fijo": input("Teléfono fijo: ").strip(),
        "estado": "Inscrito",
        "riesgo": "Bajo"
    }
    registrar_camper(camper)
    print("Camper registrado.")

def listar_campers():
    data = cargar_datos()
    return data["campers"]

def consultar_campers_por_estado(estado):
    data = cargar_datos()
    return [c for c in data["campers"] if c.get("estado") == estado]

def actualizar_estado_camper(id_camper, nuevo_estado):
    if nuevo_estado not in VALID_ESTADOS:
        raise ValueError("Estado invalido.")
    data = cargar_datos()
    camper = _find_camper(data, id_camper)
    if not camper:
        raise ValueError("Camper no encontrado.")
    camper["estado"] = nuevo_estado
    guardar_datos(data)

def marcar_camper_en_riesgo(id_camper, nivel_riesgo):
    data = cargar_datos()
    camper = _find_camper(data, id_camper)
    if not camper:
        raise ValueError("Camper no encontrado.")
    camper["riesgo"] = nivel_riesgo
    guardar_datos(data)

