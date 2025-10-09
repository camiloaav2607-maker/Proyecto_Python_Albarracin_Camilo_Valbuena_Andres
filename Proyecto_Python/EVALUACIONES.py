from ALMACENAR import cargar_datos, guardar_datos
from CAMPERS import actualizar_estado_camper, marcar_camper_en_riesgo

def _validar_nota(n):
    if not isinstance(n, (int, float)):
        raise ValueError("Nota debe ser numérica")
    if n < 0 or n > 100:
        raise ValueError("Nota fuera de rango (0-100)")

def registrar_nota_examen_inicial(id_camper, teorica, practica):
    _validar_nota(teorica); _validar_nota(practica)
    promedio = (teorica + practica) / 2
    data = cargar_datos()
    data["evaluaciones"].append({
        "id_camper": id_camper,
        "tipo": "examen_inicial",
        "teorica": teorica,
        "practica": practica,
        "promedio": promedio
    })
    if promedio >= 60:
        actualizar_estado_camper(id_camper, "Aprobado")
    guardar_datos(data)
    return promedio

def registrar_nota_modulo(id_camper, modulo, teorica, practica, quices):
    _validar_nota(teorica); _validar_nota(practica); _validar_nota(quices)
    
    nota_final = teorica * 0.3 + practica * 0.6 + quices * 0.1
    data = cargar_datos()
    data["evaluaciones"].append({
        "id_camper": id_camper,
        "tipo": "modulo",
        "modulo": modulo,
        "nota_final": nota_final
    })
    guardar_datos(data)
    
    
    if nota_final < 60:
        marcar_camper_en_riesgo(id_camper, "Alto")
        print(f"Camper {id_camper} ha quedado en Riesgo Alto por nota de modulo ({nota_final:.2f}).")
    
    return nota_final

def listar_notas_camper(id_camper):
    data = cargar_datos()
    return [e for e in data["evaluaciones"] if e["id_camper"] == id_camper]
