from ALMACENAR import cargar_datos

def reporte_campers_inscritos():
    data = cargar_datos()
    return [c for c in data["campers"] if c.get("estado") == "Inscrito"]

def reporte_campers_aprobados():
    data = cargar_datos()
    return [c for c in data["campers"] if c.get("estado") == "Aprobado"]

def reporte_trainers_activos():
    data = cargar_datos()
    return data["trainers"]

def reporte_campers_bajo_rendimiento():
    data = cargar_datos()

    campers_bajo = set()
    for e in data["evaluaciones"]:
        if e.get("tipo") == "modulo" and e.get("nota_final", 0) < 60:
            campers_bajo.add(e["id_camper"])
    return [c for c in data["campers"] if c["id"] in campers_bajo]

def reporte_asociaciones_rutas():
    data = cargar_datos()
    asociaciones = []
    for r in data["rutas"]:
        campers = [c for c in data["campers"] if c["id"] in r.get("campers", [])]
        trainers = [t for t in data["trainers"] if r["nombre"] in t.get("rutas", [])]
        asociaciones.append({
            "ruta": r["nombre"],
            "campers": campers,
            "trainers": trainers
        })
    return asociaciones

def reporte_modulos_resultados(nombre_ruta=None, id_trainer=None):
    
    data = cargar_datos()
    
    rutas = data["rutas"]
    if nombre_ruta:
        rutas = [r for r in rutas if r["nombre"].lower() == nombre_ruta.lower()]
    resultado = {}
    for r in rutas:
        for modulo in r.get("modulos", []):
            aprobados = 0
            reprobados = 0
            for e in data["evaluaciones"]:
                if e.get("tipo") == "modulo" and e.get("modulo") == modulo:
                    if e.get("nota_final", 0) >= 60:
                        aprobados += 1
                    else:
                        reprobados += 1
            resultado[f"{r['nombre']} - {modulo}"] = {"aprobados": aprobados, "reprobados": reprobados}
    return resultado             
