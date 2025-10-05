from ALMACENAR import cargar_datos, guardar_datos

def _find_trainer(data, id_trainer):
    for t in data["trainers"]:
        if t["id"] == id_trainer:
            return t
    return None

def registrar_trainer(trainer):
    data = cargar_datos()
    if _find_trainer(data, trainer["id"]):
        raise ValueError(f"Ya existe un trainer con id {trainer['id']}")
    
    if "rutas" not in trainer:
        trainer["rutas"] = []
    data["trainers"].append(trainer)
    guardar_datos(data)

def registrar_trainer_interactivo():
    trainer = {
        "id": input("ID trainer: ").strip(),
        "nombres": input("Nombres: ").strip(),
        "apellidos": input("Apellidos: ").strip(),
        "especialidad": input("Especialidad principal: ").strip(),
        "rutas": []
    }
    registrar_trainer(trainer)
    print("Trainer registrado")

def listar_trainers():
    data = cargar_datos()
    return data["trainers"]

def asignar_ruta_a_trainer(id_trainer, nombre_ruta):
    data = cargar_datos()
    trainer = _find_trainer(data, id_trainer)
    if not trainer:
        raise ValueError("Trainer no encontrado.")
    if nombre_ruta in trainer.get("rutas", []):
        return
    trainer.setdefault("rutas", []).append(nombre_ruta)
    guardar_datos(data)