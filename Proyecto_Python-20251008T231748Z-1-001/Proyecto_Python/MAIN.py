from CAMPERS import registrar_camper_interactivo, listar_campers, consultar_campers_por_estado
from TRAINERS import registrar_trainer_input, listar_trainers, asignar_ruta_trainer, encontrar_trainer
from RUTAS import listar_rutas, asignar_camper_ruta
from AREAS import listar_areas, asignar_camper_area
from MATRICULAS import crear_matricula, listar_matriculas
from EVALUACIONES import registrar_nota_examen_inicial, registrar_nota_modulo, listar_notas_camper
from REPORTES import (
    reporte_campers_inscritos, 
    reporte_campers_aprobados, 
    reporte_trainers_activos, 
    reporte_camper_bajo_rendimiento, 
    reporte_camper_riesgo_alto, 
    reporte_camper_trainer_por_ruta, 
    reporte_modulos_aprobados_perdidos 
)
from ALMACENAR import cargar_datos

def login():
    data = cargar_datos()
    print("\n===== CAMPUSLANDS LOGIN =====")
    usuario = input("Usuario: ").strip()
    clave = input("Clave: ").strip()

    for u in data.get("usuarios", []):
        if u["usuario"] == usuario and u["clave"] == clave:
            print(f"\nBienvenido {u['usuario']} ({u['rol'].upper()})")
            return u["rol"]
    print("Usuario o contraseña incorrectos.")
    return None


def menu_coordinador():
    while True:
        print("\n===== MENÚ COORDINADOR =====")
        print("1. Gestionar Campers")
        print("2. Gestionar Trainers")
        print("3. Rutas y Áreas")
        print("4. matriculas")
        print("5. Evaluaciones")
        print("6. Reportes")
        print("0. Cerrar sesión")

        op = input("opcion: ").strip()
        if op == "1": menu_campers()
        elif op == "2": menu_trainers()
        elif op == "3": menu_rutas_y_areas()
        elif op == "4": menu_matriculas()
        elif op == "5": menu_evaluaciones()
        elif op == "6": menu_reportes()
        elif op == "0": break
        else: print("opcion invalida. Intente de nuevo.")


def menu_trainer():
    while True:
        print("\n===== MENÚ TRAINER =====")
        print("1. Registrar nota de examen inicial")
        print("2. Registrar nota de modulo")
        print("3. Listar campers")
        print("0. Cerrar sesión")
        op = input("opcion: ").strip()

        try:
            if op == "1":
                id_c = input("ID camper: ").strip()
                t = float(input("Nota teorica: "))
                p = float(input("Nota práctica: "))
                prom = registrar_nota_examen_inicial(id_c, t, p)
                print(f"Nota registrada. Promedio: {prom:.2f}")
            elif op == "2":
                id_c = input("ID camper: ").strip()
                
                modulo = input("Modulo (ej: Python): ").strip()
                t = float(input("Nota teorica (30%): "))
                p = float(input("Nota practica (60%): "))
                q = float(input("Quices y trabajos (10%): "))
                nota = registrar_nota_modulo(id_c, modulo, t, p, q)
                print(f"Nota de modulo registrada. Nota Final: {nota:.2f}")
            elif op == "3":
                campers = listar_campers()
                if campers:
                    print("\n--- LISTA DE CAMPERS ---")
                    for c in campers: print(f"ID: {c['id']} | Nombre: {c['nombres']} {c['apellidos']} | Estado: {c['estado']}")
                else:
                    print("No hay campers registrados")
            elif op == "0":
                break
            else:
                print("opcion invalida.")
        except ValueError as e:
            print(f"ERROR: {e}")
        except Exception as e:
            print(f"Ocurrio un error: {e}")


def menu_camper():
    while True:
        print("\n===== MENÚ CAMPER =====")
        print("1. Consultar mis notas")
        print("2. Consultar campers por estado (general)")
        print("0. Cerrar sesión")

        op = input("opcion: ").strip()
        if op == "1":
            id_c = input("Ingrese su ID: ").strip()
            notas = listar_notas_camper(id_c)
            if notas:
                print("\n--- MIS NOTAS ---")
                for n in notas: 
                    print(f"Tipo: {n['tipo']} | modulo: {n.get('modulo', 'Inicial')} | Nota: {n.get('promedio', n.get('nota_final')):.2f}")
            else:
                print("No tiene notas registradas aún.")
        elif op == "2":
            estado = input("Estado a consultar (ej: Inscrito, Aprobado): ").strip()
            campers = consultar_campers_por_estado(estado)
            if campers:
                print(f"\n--- CAMPERS EN ESTADO '{estado.upper()}' ---")
                for c in campers: print(f"ID: {c['id']} | Nombre: {c['nombres']} {c['apellidos']}")
            else:
                print("No hay campers con ese estado.")
        elif op == "0":
            break
        else:
            print("opcion invalida.")


def menu_campers():
    while True:
        print("\n--- GESTIÓN DE CAMPERS ---")
        print("1. Registrar camper (Estado inicial: Inscrito)")
        print("2. Listar todos los campers")
        print("3. Consultar por estado")
        print("0. Volver")
        op = input("opcion: ").strip()

        if op == "1": registrar_camper_interactivo()
        elif op == "2":
            campers = listar_campers()
            if campers:
                print("\n--- TODOS LOS CAMPERS ---")
                for c in campers: 
                    print(f"ID: {c['id']} | Nombre: {c['nombres']} | Estado: {c['estado']} | Riesgo: {c['riesgo']}")
            else:
                print("No hay campers registrados.")
        elif op == "3":
            estado = input("Estado (ej: Aprobado, Cursando): ").strip()
            campers = consultar_campers_por_estado(estado)
            if campers:
                print(f"\n--- CAMPERS EN ESTADO '{estado.upper()}' ---")
                for c in campers: print(f"ID: {c['id']} | Nombre: {c['nombres']} {c['apellidos']}")
            else:
                print("No hay campers en ese estado.")
        elif op == "0": break
        else: print("opcion invalida.")


def menu_trainers():
    while True:
        print("\n--- GESTION DE TRAINERS ---")
        print("1. Registrar trainer")
        print("2. Listar trainers")
        print("3. Asignar ruta a trainer")
        print("0. Volver")
        op = input("opcion: ").strip()

        try:
            if op == "1": registrar_trainer_input()
            elif op == "2":
                trainers = listar_trainers()
                if trainers:
                    print("\n--- TODOS LOS TRAINERS ---")
                    for t in trainers: print(f"ID: {t['id']} | Nombre: {t['nombres']} {t['apellidos']} | Rutas: {', '.join(t['rutas'])}")
                else:
                    print("No hay trainers registrados.")
            elif op == "3":
                id_t = input("ID trainer: ").strip()
                ruta = input("Ruta a asignar (Fundamentos-Backend-Fronted): ").strip()
                asignar_ruta_trainer(id_t, ruta)
                print("Ruta asignada.")
            elif op == "0": break
            else: print("opcion invalida.")
        except ValueError as e:
            print(f"ERROR: {e}")


def menu_rutas_y_areas():
    while True:
        print("\n--- RUTAS Y ÁREAS ---")
        print("1. Listar rutas disponibles")
        print("2. Asignar camper a ruta (Solo asignación lógica, no matricula)")
        print("3. Listar áreas de entrenamiento")
        print("4. Asignar camper a área (Salón)")
        print("0. Volver")
        op = input("opcion: ").strip()

        try:
            if op == "1":
                print("\n--- RUTAS ---")
                for r in listar_rutas(): 
                    print(f"Nombre: {r['nombre']} | modulos: {', '.join(r['modulos'])}")
            elif op == "2":
                id_c = input("ID camper: ").strip()
                ruta = input("Ruta: ").strip()
                asignar_camper_ruta(id_c, ruta)
            elif op == "3":
                print("\n--- ÁREAS ---")
                for a in listar_areas(): 
                    print(f"Nombre: {a['nombre']} | Capacidad: {len(a['campers'])}/{a['capacidad']}")
            elif op == "4":
                id_c = input("ID camper: ").strip()
                area = input("Área (ej: Desarrollo Web): ").strip()
                asignar_camper_area(id_c, area)
            elif op == "0": break
            else: print("opcion invalida.")
        except ValueError as e:
            print(f"ERROR: {e}")


def menu_matriculas():
    while True:
        print("\n--- MATRICULAS ---")
        print("1. Crear matríc" \
        "ula (Asigna camper 'Aprobado' a ruta/trainer/área y lo cambia a 'Cursando')")
        print("2. Listar matriculas")
        print("0. Volver")
        op = input("opcion: ").strip()

        try:
            if op == "1":
                id_c = input("ID camper: ").strip()
                ruta = input("Ruta (Fundamentos-Backend-Fronted): ").strip()
                area = input("Area/Salon (Desarrollo Web-Desarrollo Movil-Desarrollo de Videojuegos): ").strip()
                
                
                id_t = input("ID Trainer encargado (debe tener la ruta asignada): ").strip()
                f_inicio = input("Fecha inicio (DD/MM/AAAA): ").strip()
                f_fin = input("Fecha finalización (DD/MM/AAAA): ").strip()
                
                
                crear_matricula(id_c, ruta, area, id_t, f_inicio, f_fin)
            elif op == "2":
                print("\n--- LISTA DE MATRICULAS ---")
                for m in listar_matriculas(): 
                    print(f"Camper: {m['id_camper']} | Ruta: {m['ruta']} | Trainer: {m['id_trainer']} | Área: {m['area']} | Inicio: {m['fecha_inicio']}")
            elif op == "0": break
            else: print("opcion invalida.")
        except ValueError as e:
            print(f"ERROR: {e}")


def menu_evaluaciones():
    while True:
        print("\n--- EVALUACIONES ---")
        print("1. Registrar examen inicial (Solo para cambiar estado a 'Aprobado')")
        print("2. Registrar nota de modulo (Aplica peso y marca riesgo si es < 60)")
        print("0. Volver")
        op = input("opcion: ").strip()
        
        try:
            if op == "1":
                id_c = input("ID camper: ").strip()
                t = float(input("Nota teorica (0-100): "))
                p = float(input("Nota práctica (0-100): "))
                prom = registrar_nota_examen_inicial(id_c, t, p)
                print(f"Nota registrada. Promedio: {prom:.2f}")
            elif op == "2":
                id_c = input("ID camper: ").strip()
                modulo = input("Modulo: ").strip()
                t = float(input("Teorica (0-100): "))
                p = float(input("Práctica (0-100): "))
                q = float(input("Quices/Trabajos (0-100): "))
                nota = registrar_nota_modulo(id_c, modulo, t, p, q)
                print(f"Nota de modulo registrada. Nota Final: {nota:.2f}")
            elif op == "0": break
            else: print("opcion invalida.")
        except ValueError as e:
            print(f"ERROR: {e}")


def menu_reportes():
    while True:
        print("\n--- REPORTES ---")
        print("1. Campers en estado de **Inscrito**.")
        print("2. Campers que **Aprobaron** el examen inicial.")
        print("3. Trainers que se encuentran **trabajando** (activos).")
        print("4. Campers con **Bajo Rendimiento** (nota modulo < 60).")
        print("5. Campers en **Riesgo Alto**.")
        print("6. Campers y Trainers asociados a una ruta.")
        print("7. modulos Aprobados/Perdidos por Ruta y Trainer.")
        print("0. Volver")
        op = input("opcion: ").strip()

        if op == "1":
            print("\n--- CAMPERS INSCRITOS ---")
            for c in reporte_campers_inscritos(): print(c)
        elif op == "2":
            print("\n--- CAMPERS APROBADOS ---")
            for c in reporte_campers_aprobados(): print(c)
        elif op == "3":
            print("\n--- TRAINERS ACTIVOS ---")
            for t in reporte_trainers_activos(): print(t)
        elif op == "4":
            print("\n--- CAMPERS BAJO RENDIMIENTO ---")
            for c in reporte_camper_bajo_rendimiento(): print(c)
        elif op == "5":
            print("\n--- CAMPERS EN RIESGO ALTO ---")
            for c in reporte_camper_riesgo_alto(): print(c)
        elif op == "6":
            ruta = input("Nombre de la ruta a consultar: ").strip()
            reporte_camper_trainer_por_ruta(ruta)
        elif op == "7":
            ruta = input("Nombre de la ruta a analizar (ej: Ruta Java): ").strip()
            reporte_modulos_aprobados_perdidos(ruta)
        elif op == "0": break
        else: print("opcion invalida.")


if __name__ == "__main__":
    while True:
        rol = login()
        if rol == "coordinador":
            menu_coordinador()
        elif rol == "trainer":
            menu_trainer()
        elif rol == "camper":
            menu_camper()
        else:
            print("Saliendo del sistema...")
            break