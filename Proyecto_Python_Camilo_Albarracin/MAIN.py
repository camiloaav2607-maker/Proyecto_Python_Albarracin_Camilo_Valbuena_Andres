from CAMPERS import registrar_camper_interactivo, listar_campers, consultar_campers_por_estado
from TRAINERS import registrar_trainer_interactivo, listar_trainers, asignar_ruta_a_trainer
from RUTAS import crear_ruta_interactiva, listar_rutas, asignar_camper_a_ruta
from AREAS import crear_area_interactiva, listar_areas, asignar_camper_a_area
from MATRICULAS import crear_matricula_interactiva, listar_matriculas
from EVALUACIONES import registrar_nota_examen_inicial, registrar_nota_modulo, evaluar_rendimiento_camper
from REPORTES import (reporte_campers_inscritos, reporte_campers_aprobados,
                    reporte_trainers_activos, reporte_campers_bajo_rendimiento,
                    reporte_asociaciones_rutas, reporte_modulos_resultados)

def menu_principal():
    while True:
        print("\n--- CampusLands - Menú Principal ---")
        print("1. Campers")
        print("2. Trainers")
        print("3. Rutas")
        print("4. Areas")
        print("5. Matrículas")
        print("6. Evaluaciones")
        print("7. Reportes")
        print("0. Salir")
        op = input("Opcion: ").strip()
        if op == "1":
            menu_campers()
        elif op == "2":
            menu_trainers()
        elif op == "3":
            menu_rutas()
        elif op == "4":
            menu_areas()
        elif op == "5":
            menu_matriculas()
        elif op == "6":
            menu_evaluaciones()
        elif op == "7":
            menu_reportes()
        elif op == "0":
            print("Adios")
            break
        else:
            print("Opcion invalida")

def menu_campers():
    while True:
        print("\n--- Campers ---")
        print("1. Registrar camper")
        print("2. Listar campers")
        print("3. Consultar por estado")
        print("0. Volver")
        op = input("Opcion: ").strip()
        if op == "1":
            try:
                registrar_camper_interactivo()
            except Exception as e:
                print("Error:", e)
        elif op == "2":
            for c in listar_campers():
                print(c)
        elif op == "3":
            estado = input("Estado: ").strip()
            for c in consultar_campers_por_estado(estado):
                print(c)
        elif op == "0":
            return
        else:
            print("Opcion invalida")

def menu_trainers():
    while True:
        print("\n--- Trainers ---")
        print("1. Registrar trainer")
        print("2. Listar trainers")
        print("3. Asignar ruta a trainer")
        print("0. Volver")
        op = input("Opcion: ").strip()
        if op == "1":
            try:
                registrar_trainer_interactivo()
            except Exception as e:
                print("Error:", e)
        elif op == "2":
            for t in listar_trainers():
                print(t)
        elif op == "3":
            id_t = input("ID trainer: ").strip()
            ruta = input("Nombre ruta: ").strip()
            try:
                asignar_ruta_a_trainer(id_t, ruta)
                print("Ruta asignada")
            except Exception as e:
                print("Error:", e)
        elif op == "0":
            return
        else:
            print("Opcion invalida")

def menu_rutas():
    while True:
        print("\n--- Rutas ---")
        print("1. Crear ruta")
        print("2. Listar rutas")
        print("3. Asignar camper a ruta")
        print("0. Volver")
        op = input("Opcion: ").strip()
        if op == "1":
            try:
                crear_ruta_interactiva()
            except Exception as e:
                print("Error:", e)
        elif op == "2":
            for r in listar_rutas():
                print(r)
        elif op == "3":
            id_c = input("ID camper: ").strip()
            ruta = input("Nombre ruta: ").strip()
            try:
                asignar_camper_a_ruta(id_c, ruta)
                print("Camper asignado a ruta")
            except Exception as e:
                print("Error:", e)
        elif op == "0":
            return
        else:
            print("Opcion invalida")

def menu_areas():
    while True:
        print("\n--- Areas ---")
        print("1. Crear area")
        print("2. Listar areas")
        print("3. Asignar camper a area")
        print("0. Volver")
        op = input("Opcion: ").strip()
        if op == "1":
            try:
                crear_area_interactiva()
            except Exception as e:
                print("Error:", e)
        elif op == "2":
            for a in listar_areas():
                print(a)
        elif op == "3":
            id_c = input("ID camper: ").strip()
            area = input("Nombre area: ").strip()
            try:
                asignar_camper_a_area(id_c, area)
                print("Camper asignado al area")
            except Exception as e:
                print("Error:", e)
        elif op == "0":
            return
        else:
            print("Opcion invalida")

def menu_matriculas():
    while True:
        print("\n--- Matrículas ---")
        print("1. Crear matrícula")
        print("2. Listar matrículas")
        print("0. Volver")
        op = input("Opcion: ").strip()
        if op == "1":
            try:
                crear_matricula_interactiva()
            except Exception as e:
                print("Error:", e)
        elif op == "2":
            for m in listar_matriculas():
                print(m)
        elif op == "0":
            return
        else:
            print("Opcion invalida")

def menu_evaluaciones():
    while True:
        print("\n--- Evaluaciones ---")
        print("1. Registrar nota examen inicial")
        print("2. Registrar nota modulo")
        print("3. Evaluar rendimiento camper (calcula riesgo)")
        print("0. Volver")
        op = input("Opcion: ").strip()
        if op == "1":
            id_c = input("ID camper: ").strip()
            t = float(input("Nota teorica (0-100): ").strip())
            p = float(input("Nota practica (0-100): ").strip())
            try:
                prom = registrar_nota_examen_inicial(id_c, t, p)
                print("Promedio examen inicial:", prom)
            except Exception as e:
                print("Error:", e)
        elif op == "2":
            id_c = input("ID camper: ").strip()
            modulo = input("Modulo: ").strip()
            t = float(input("Teorica (0-100): ").strip())
            p = float(input("Practica (0-100): ").strip())
            q = float(input("Quices y trabajos (0-100): ").strip())
            try:
                nota = registrar_nota_modulo(id_c, modulo, t, p, q)
                print("Nota final modulo:", nota)
            except Exception as e:
                print("Error:", e)
        elif op == "3":
            id_c = input("ID camper: ").strip()
            try:
                riesgo = evaluar_rendimiento_camper(id_c)
                print("Riesgo actualizado:", riesgo)
            except Exception as e:
                print("Error:", e)
        elif op == "0":
            return
        else:
            print("Opcion invalida")

def menu_reportes():
    while True:
        print("\n--- Reportes ---")
        print("1. Campers inscritos")
        print("2. Campers aprobados")
        print("3. Trainers activos")
        print("4. Campers bajo rendimiento")
        print("5. Asociaciones rutas (campers & trainers)")
        print("6. Resultados módulos por ruta")
        print("0. Volver")
        op = input("Opcion: ").strip()
        if op == "1":
            for c in reporte_campers_inscritos():
                print(c)
        elif op == "2":
            for c in reporte_campers_aprobados():
                print(c)
        elif op == "3":
            for t in reporte_trainers_activos():
                print(t)
        elif op == "4":
            for c in reporte_campers_bajo_rendimiento():
                print(c)
        elif op == "5":
            for a in reporte_asociaciones_rutas():
                print(a)
        elif op == "6":
            ruta = input("Nombre ruta (opcional): ").strip() or None
            res = reporte_modulos_resultados(ruta)
            for k, v in res.items():
                print(k, v)
        elif op == "0":
            return
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    menu_principal()                                      






























