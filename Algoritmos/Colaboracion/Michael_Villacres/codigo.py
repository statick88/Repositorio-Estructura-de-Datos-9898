class LigaBarrial:
    def __init__(self, nombre, anio):
        self.nombre = nombre
        self.anio = anio


    def __str__(self):
        return f"{self.nombre} ({self.anio}) "


def mostrar_jugadores(jugadores):
    if jugadores:
        print("Jugadores ingresados:")
        for jugador in jugadores:
            print(jugadores)
    else:
        print("No se ha ingresado ningun jugador.")


def eliminar_jugadores(jugadores):
    if jugadores:
        nombre = input("Ingrese el nombre del jugador a eliminar: ")
        jugadores_filtrados = [jugador for jugador in jugadores if jugador.nombre != nombre]
        if len(jugadores_filtrados) < len(jugadores):
            jugadores[:] = jugadores_filtrados
            print("Jugador eliminado exitosamente.")
        else:
            print("No se encontró ningun jugador con ese nombre!!!!!!")
    else:
        print("No se han ingresado jugadores")



def modificar_jugadores(jugadores):
    if jugadores:
        nombre = input("Ingrese el nombre del jugador a modificar: ")
        for jugador in jugadores:
            if jugador.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre del jugador: ")
                nuevo_anio = int(input("Ingrese el nuevo año del jugador: "))
                jugador.nombre = nuevo_nombre
                jugador.anio = nuevo_anio
                print("Jugador modificado exitosamente")
                return
        print("No se encontró ningun jugador con ese nombre")
    else:
        print("No se han ingresado jugadores")


def ordenar_jugadores(jugadores, criterio):
    if jugadores:
        if criterio == "nombre":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                jugadores.sort(key=lambda jugador: jugador.nombre)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por nombre
                def shell_sort_nombre(jugadores):
                    n = len(jugadores)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = jugadores[i]
                            j = i

                            while j >= gap and jugadores[j - gap].nombre > temp.nombre:
                                jugadores[j] = jugadores[j - gap]
                                j -= gap

                            jugadores[j] = temp

                        gap //= 2

                shell_sort_nombre(jugadores)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por nombre
                def partition_nombre(jugadores, low, high):
                    pivot = jugadores[high].nombre
                    i = low - 1

                    for j in range(low, high):
                        if jugadores[j].nombre < pivot:
                            i += 1
                            jugadores[i], jugadores[j] = jugadores[j], jugadores[i]

                    jugadores[i + 1], jugadores[high] = jugadores[high], jugadores[i + 1]
                    return i + 1

                def quick_sort_nombre(jugadores, low, high):
                    if low < high:
                        pivot_index = partition_nombre(jugadores, low, high)
                        quick_sort_nombre(jugadores, low, pivot_index - 1)
                        quick_sort_nombre(jugadores, pivot_index + 1, high)

                quick_sort_nombre(jugadores, 0, len(jugadores) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        elif criterio == "anio":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                jugadores.sort(key=lambda jugadores: jugadores.anio)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por año
                def shell_sort_anio(jugadores):
                    n = len(jugadores)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = jugadores[i]
                            j = i

                            while j >= gap and jugadores[j - gap].anio > temp.anio:
                                jugadores[j] = jugadores[j - gap]
                                j -= gap

                            jugadores[j] = temp

                        gap //= 2

                shell_sort_anio(jugadores)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por año
                def partition_anio(jugadores, low, high):
                    pivot = jugadores[high].anio
                    i = low - 1

                    for j in range(low, high):
                        if jugadores[j].anio < pivot:
                            i += 1
                            jugadores[i], jugadores[j] = jugadores[j], jugadores[i]

                    jugadores[i + 1], jugadores[high] = jugadores[high], jugadores[i + 1]
                    return i + 1

                def quick_sort_anio(jugadores, low, high):
                    if low < high:
                        pivot_index = partition_anio(jugadores, low, high)
                        quick_sort_anio(jugadores, low, pivot_index - 1)
                        quick_sort_anio(jugadores, pivot_index + 1, high)

                quick_sort_anio(jugadores, 0, len(jugadores) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        else:
            print("Criterio de ordenamiento inválido.")
    else:
        print("No se han ingresado películas.")


def menu():
    peliculas = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar jugador")
        print("2. Mostrar jugador")
        print("3. Eliminar jugador")
        print("4. Modificar jugador")
        print("5. Ordenar jugador por nombre")
        print("6. Ordenar jugador por año")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del jugador: ")
            anio = int(input("Ingrese el año del jugador: "))
            jugadores = LigaBarrial(nombre, anio)
            jugadores.append(jugadores)
            print("JUgador ingresado exitosamente")
        elif opcion == "2":
            mostrar_jugadores(jugadores)
        elif opcion == "3":
            eliminar_jugadores(jugadores)
        elif opcion == "4":
            modificar_jugadores(jugadores)
        elif opcion == "5":
            ordenar_jugadores(jugadores, "nombre")
        elif opcion == "6":
            ordenar_jugadores(jugadores, "anio")
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()