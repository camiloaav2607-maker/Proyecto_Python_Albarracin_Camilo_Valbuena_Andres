from ALMACENAR import cargar_datos, guardar_datos

def encontrar_trainer(data, id_trainer):
    for t in data["trainers"]:
        if t["id"] == id_trainer:
            return t
    return None

def registrar_trainer(trainer):
    data = cargar_datos()
    if encontrar_trainer(data, trainer["id"]):
        raise ValueError(f"Ya existe un trainer con ID {trainer['id']}")
    trainer.setdefault("rutas", [])
    data["trainers"].append(trainer)
    guardar_datos(data)

def registrar_trainer_input():
    trainer = {
        "id": input("ID trainer: ").strip(),
        "nombres": input("Nombres: ").strip(),
        "apellidos": input("Apellidos: ").strip(),
        "especialidad": input("Especialidad: ").strip(),
        "rutas": []
    }
    registrar_trainer(trainer)
    print("Trainer registrado.")

def listar_trainers():
    data = cargar_datos()
    return data.get("trainers", [])

def asignar_ruta_trainer(id_trainer, nombre_ruta):
    data = cargar_datos()
    trainer = encontrar_trainer(data, id_trainer)
    if not trainer:
        raise ValueError("Trainer no encontrado.")
    if nombre_ruta not in trainer["rutas"]:
        trainer["rutas"].append(nombre_ruta)
    guardar_datos(data)