from ALMACENAR import cargar_datos, guardar_datos
from CAMPERS import actualizar_estado_camper

def _validar_nota(n):
    if not isinstance(n, (int, float)):
        raise ValueError("Nota debe ser numero")
    if n < 0 or n > 100:
        raise ValueError("Nota fuera de rango 0-100")

def calcular_promedio_inicial(teorica, practica):
    _validar_nota(teorica); _validar_nota(practica)
    return (teorica + practica) / 2

def registrar_nota_examen_inicial(id_camper, teorica, practica):
    promedio = calcular_promedio_inicial(teorica, practica)
    data = cargar_datos()
    data["evaluaciones"].append({
        "id_camper": id_camper,
        "tipo": "examen_inicial",
        "teorica": teorica,
        "practica": practica,
        "promedio": promedio
    })
    
    if promedio >= 60:
        try:
            actualizar_estado_camper(id_camper, "Aprobado")
        except Exception:

            pass
    guardar_datos(data)
    return promedio

def calcular_nota_modulo(teorica, practica, quices):
    _validar_nota(teorica); _validar_nota(practica); _validar_nota(quices)

    return teorica * 0.3 + practica * 0.6 + quices * 0.1

def registrar_nota_modulo(id_camper, modulo, teorica, practica, quices):
    nota_final = calcular_nota_modulo(teorica, practica, quices)
    data = cargar_datos()
    data["evaluaciones"].append({
        "id_camper": id_camper,
        "tipo": "modulo",
        "modulo": modulo,
        "teorica": teorica,
        "practica": practica,
        "quices": quices,
        "nota_final": nota_final
    })
    guardar_datos(data)
    return nota_final

def evaluar_rendimiento_camper(id_camper):
    data = cargar_datos()
    notas = [e["nota_final"] for e in data["evaluaciones"] if e["id_camper"] == id_camper and e["tipo"] == "modulo"]
    if not notas:
        return None

    if any(n < 60 for n in notas):
        from CAMPERS import marcar_camper_en_riesgo
        marcar_camper_en_riesgo(id_camper, "Alto")
        return "Alto"
    else:
        from CAMPERS import marcar_camper_en_riesgo
        marcar_camper_en_riesgo(id_camper, "Bajo")
        return "Bajo"

def listar_campers_en_riesgo():
    data = cargar_datos()
    return [c for c in data["campers"] if c.get("riesgo") == "Alto"]