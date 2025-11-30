# ---------------------------
# Funciones de apoyo
# ---------------------------

def mostrar_menu():
    print("\n--- Gestor de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")


def pedir_opcion():
    while True:
        opcion = input("Elige una opción: ")

        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= 5:
                return opcion

        print("Opción inválida. Debe ser un número del 1 al 5.")


def mostrar_tareas(tareas):
    if not tareas:
        print("\nNo hay tareas registradas.")
        return

    print("\n--- Lista de tareas ---")
    for i, tarea in enumerate(tareas, start=1):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"{i}. {tarea['descripcion']}  [{estado}]")


def pedir_numero_tarea(tareas, mensaje):
    if not tareas:
        print("No hay tareas.")
        return None

    mostrar_tareas(tareas)
    print("(0 para cancelar)")

    while True:
        numero = input(mensaje)

        if numero.isdigit():
            numero = int(numero)

            if numero == 0:
                return None

            if 1 <= numero <= len(tareas):
                return numero - 1

        print("Número inválido.")


# ---------------------------
# Funciones principales
# ---------------------------

def agregar_tarea(tareas):
    descripcion = input("\nDescripción de la tarea: ").strip()

    if not descripcion:
        print("La descripción no puede estar vacía.")
        return

    tarea = {"descripcion": descripcion, "completada": False}
    tareas.append(tarea)
    print("Tarea agregada correctamente.")


def marcar_como_completada(tareas):
    indice = pedir_numero_tarea(tareas, "Número de tarea a completar: ")

    if indice is None:
        print("Cancelado.")
        return

    tareas[indice]["completada"] = True
    print("Tarea marcada como completada.")


def eliminar_tarea(tareas):
    indice = pedir_numero_tarea(tareas, "Número de tarea a eliminar: ")

    if indice is None:
        print("Cancelado.")
        return

    eliminada = tareas.pop(indice)
    print(f"Tarea eliminada: {eliminada['descripcion']}")


# ---------------------------
# Programa principal
# ---------------------------

def main():
    tareas = []  

    while True:
        mostrar_menu()
        opcion = pedir_opcion()

        if opcion == 1:
            agregar_tarea(tareas)
        elif opcion == 2:
            mostrar_tareas(tareas)
        elif opcion == 3:
            marcar_como_completada(tareas)
        elif opcion == 4:
            eliminar_tarea(tareas)
        elif opcion == 5:
            print("Saliendo... ¡Hasta luego!")
            break


main()
