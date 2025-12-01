from datetime import datetime


def pedir_texto(mensaje: str) -> str:
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Este campo no puede estar vacío. Intenta nuevamente.")


def pedir_float(mensaje: str) -> float:
    while True:
        valor = input(mensaje).strip().replace(",", ".")
        try:
            numero = float(valor)
            if numero < 0:
                print("El número no puede ser negativo.")
                continue
            return numero
        except ValueError:
            print("Debes ingresar un número válido (ej: 1.5).")


def pedir_opcion(mensaje: str, opciones_validas: dict) -> str:
    while True:
        print(mensaje)
        for clave, etiqueta in opciones_validas.items():
            print(f"  {clave}) {etiqueta}")
        eleccion = input("Elige una opción: ").strip()
        if eleccion in opciones_validas:
            return opciones_validas[eleccion]
        print("Opción no válida, intenta nuevamente.")


def pedir_fecha_opcional(mensaje: str):
    while True:
        valor = input(mensaje + " (DD-MM-YYYY, vacío = sin fecha): ").strip()
        if not valor:
            return None
        try:
            fecha = datetime.strptime(valor, "%d-%m-%Y").date()
            return fecha
        except ValueError:
            print("Formato de fecha inválido. Usa DD-MM-YYYY.")


def clasificar_vencimiento(fecha_limite):
    if fecha_limite is None:
        return "Sin fecha"

    hoy = datetime.today().date()
    diferencia = (fecha_limite - hoy).days

    if diferencia < 0:
        return "Vencida"
    elif diferencia == 0:
        return "Para hoy"
    elif 1 <= diferencia <= 3:
        return "Próximos días"
    else:
        return "Futura"


def crear_tarea() -> dict:
    print("\n Nueva tarea")
    titulo = pedir_texto("Título de la tarea: ")
    descripcion = pedir_texto("Descripción breve: ")
    prioridad = pedir_opcion(
        "Prioridad de la tarea:",
        {"1": "Alta", "2": "Media", "3": "Baja"}
    )
    horas_estimadas = pedir_float("Horas estimadas para completar la tarea: ")
    fecha_limite = pedir_fecha_opcional("Fecha límite")

    
    es_tarea_grande = horas_estimadas >= 8

    estado_vencimiento = clasificar_vencimiento(fecha_limite)

    tarea = {
        "titulo": titulo,
        "descripcion": descripcion,
        "prioridad": prioridad,
        "horas_estimadas": horas_estimadas,
        "fecha_limite": fecha_limite,
        "es_tarea_grande": es_tarea_grande,
        "estado_vencimiento": estado_vencimiento,
    }

    print("Tarea creada correctamente.")
    return tarea


def mostrar_resumen(tablero_nombre: str, tareas: list):
    print("\n" + "=" * 60)
    print(f"Resumen del tablero: {tablero_nombre}")
    print("=" * 60)

    if not tareas:
        print("No se crearon tareas en este tablero.")
        return

    total_tareas = len(tareas)
    total_horas = 0.0
    conteo_prioridad = {"Alta": 0, "Media": 0, "Baja": 0}

    for tarea in tareas:
        total_horas += tarea["horas_estimadas"]
        if tarea["prioridad"] in conteo_prioridad:
            conteo_prioridad[tarea["prioridad"]] += 1

    print(f"Total de tareas: {total_tareas}")
    print(f"Horas estimadas totales: {total_horas:.2f}")

    print("\nTareas por prioridad:")
    for prioridad, cantidad in conteo_prioridad.items():
        print(f"  - {prioridad}: {cantidad} tarea(s)")

    print("\nDetalle de tareas:\n")
    for idx, tarea in enumerate(tareas, start=1):
        fecha_txt = (
            tarea["fecha_limite"].strftime("%d-%m-%Y")
            if tarea["fecha_limite"] is not None
            else "Sin fecha"
        )
        grande_txt = "Sí" if tarea["es_tarea_grande"] else "No"

        print(f"{idx}. {tarea['titulo']}")
        print(f"   Descripción      : {tarea['descripcion']}")
        print(f"   Prioridad        : {tarea['prioridad']}")
        print(f"   Horas estimadas  : {tarea['horas_estimadas']:.2f}")
        print(f"   Fecha límite     : {fecha_txt}")
        print(f"   Estado vencimiento: {tarea['estado_vencimiento']}")
        print(f"   ¿Tarea grande?   : {grande_txt}")
        print("-" * 60)


def main():
    print("=" * 60)
    print("🐾 Chungungo Kanban – Gestor básico por consola (Módulo 4)")
    print("=" * 60)

    tablero_nombre = pedir_texto("Nombre del tablero: ")

    tareas = []  

    while True:
        tarea = crear_tarea()
        tareas.append(tarea)

        continuar = input("\n¿Quieres agregar otra tarea? (s/n): ").strip().lower()
        if continuar != "s":
            break

    mostrar_resumen(tablero_nombre, tareas)

    print("\nGracias por usar el gestor básico de Chungungo Kanban.")

if __name__ == "__main__":
    main()
