class Deporte:
    def __init__(self, nombre, anio):
        self.nombre = nombre
        self.anio = anio

    def __str__(self):
        return f"{self.nombre} ({self.anio})"


def mostrar_deportes(deportes):
    if deportes:
        print("Deportes ingresados:")
        for deporte in deportes:
            print(deporte)
    else:
        print("No se han ingresado deportes.")


def eliminar_deporte(deportes):
    if deportes:
        nombre = input("Ingrese el nombre del deporte a eliminar: ")
        deportes_filtrados = [deporte for deporte in deportes if deporte.nombre != nombre]
        if len(deportes_filtrados) < len(deportes):
            deportes[:] = deportes_filtrados
            print("Deporte eliminado exitosamente.")
        else:
            print("No se encontró un deporte con ese nombre.")
    else:
        print("No se han ingresado deportes.")


def modificar_deporte(deportes):
    if deportes:
        nombre = input("Ingrese el nombre del deporte a modificar: ")
        for deporte in deportes:
            if deporte.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre del deporte: ")
                nuevo_anio = int(input("Ingrese el nuevo año del deporte: "))
                deporte.nombre = nuevo_nombre
                deporte.anio = nuevo_anio
                print("Deporte modificado exitosamente.")
                return
        print("No se encontró un deporte con ese nombre.")
    else:
        print("No se han ingresado deportes.")


def ordenar_deportes(deportes, criterio):
    if deportes:
        if criterio == "nombre":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                deportes.sort(key=lambda deporte: deporte.nombre)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por nombre
                def shell_sort_nombre(deportes):
                    n = len(deportes)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = deportes[i]
                            j = i

                            while j >= gap and deportes[j - gap].nombre > temp.nombre:
                                deportes[j] = deportes[j - gap]
                                j -= gap

                            deportes[j] = temp

                        gap //= 2

                shell_sort_nombre(deportes)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por nombre
                def partition_nombre(deportes, low, high):
                    pivot = deportes[high].nombre
                    i = low - 1

                    for j in range(low, high):
                        if deportes[j].nombre < pivot:
                            i += 1
                            deportes[i], deportes[j] = deportes[j], deportes[i]

                    deportes[i + 1], deportes[high] = deportes[high], deportes[i + 1]
                    return i + 1

                def quick_sort_nombre(deportes, low, high):
                    if low < high:
                        pivot_index = partition_nombre(deportes, low, high)
                        quick_sort_nombre(deportes, low, pivot_index - 1)
                        quick_sort_nombre(deportes, pivot_index + 1, high)

                quick_sort_nombre(deportes, 0, len(deportes) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        elif criterio == "anio":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                deportes.sort(key=lambda pelicula: pelicula.anio)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por año
                def shell_sort_anio(deportes):
                    n = len(deportes)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = peliculas[i]
                            j = i

                            while j >= gap and deportes[j - gap].anio > temp.anio:
                                deportes[j] = deportes[j - gap]
                                j -= gap

                            deportes[j] = temp

                        gap //= 2

                shell_sort_anio(deportes)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por año
                def partition_anio(deportes, low, high):
                    pivot = deportes[high].anio
                    i = low - 1

                    for j in range(low, high):
                        if deportes[j].anio < pivot:
                            i += 1
                            deportes[i], deportes[j] = deportes[j], deportes[i]

                    deportes[i + 1], deportes[high] = deportes[high], deportes[i + 1]
                    return i + 1

                def quick_sort_anio(deportes, low, high):
                    if low < high:
                        pivot_index = partition_anio(deportes, low, high)
                        quick_sort_anio(deportes, low, pivot_index - 1)
                        quick_sort_anio(deportes, pivot_index + 1, high)

                quick_sort_anio(deportes, 0, len(deportes) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        else:
            print("Criterio de ordenamiento inválido.")
    else:
        print("No se han ingresado películas.")
        

def menu():
    deportes = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar deporte")
        print("2. Mostrar deportes")
        print("3. Eliminar deporte")
        print("4. Modificar deporte")
        print("5. Ordenar deportes por nombre")
        print("6. Ordenar deportes por año")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del deporte: ")
            anio = int(input("Ingrese el año del deporte: "))
            deporte = Deporte(nombre, anio)
            deportes.append(deporte)
            print("Deporte ingresado exitosamente.")
        elif opcion == "2":
            mostrar_deportes(deportes)
        elif opcion == "3":
            eliminar_deporte(deportes)
        elif opcion == "4":
            modificar_deporte(deportes)
        elif opcion == "5":
            ordenar_deportes(deportes, "nombre")
        elif opcion == "6":
            ordenar_deportes(deportes, "anio")
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()