class Videojuego:
    def __init__(self, nombre, anio):
        self.nombre = nombre
        self.anio = anio

    def __str__(self):
        return f"{self.nombre} ({self.anio})"


def mostrar_videojuegos(videojuegos):
    if videojuegos:
        print("Videojuegos ingresadas:")
        for videojuego in videojuegos:
            print(videojuego)
    else:
        print("No se han ingresado videojuegos.")


def eliminar_videojuego(videojuegos):
    if videojuegos:
        nombre = input("Ingrese el nombre de la videojuego a eliminar: ")
        videojuegos_filtradas = [videojuego for videojuego in videojuegos if videojuego.nombre != nombre]
        if len(videojuegos_filtradas) < len(videojuegos):
            videojuegos[:] = videojuegos_filtradas
            print("Videojuegos eliminada exitosamente.")
        else:
            print("No se encontró una videojuego con ese nombre.")
    else:
        print("No se han ingresado videojuegos.")



def modificar_videojuego(videojuegos):
    if videojuegos:
        nombre = input("Ingrese el nombre de la videojuego a modificar: ")
        for videojuego in videojuegos:
            if videojuego.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre de la videojuego: ")
                nuevo_anio = int(input("Ingrese el nuevo año de la videojuego: "))
                videojuego.nombre = nuevo_nombre
                videojuego.anio = nuevo_anio
                print("Videojuegos modificada exitosamente.")
                return
        print("No se encontró una videojuego con ese nombre.")
    else:
        print("No se han ingresado videojuegos.")


def ordenar_videojuegos(videojuegos, criterio):
    if videojuegos:
        if criterio == "nombre":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                videojuegos.sort(key=lambda videojuego: videojuego.nombre)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por nombre
                def shell_sort_nombre(videojuegos):
                    n = len(videojuegos)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = videojuegos[i]
                            j = i

                            while j >= gap and videojuegos[j - gap].nombre > temp.nombre:
                                videojuegos[j] = videojuegos[j - gap]
                                j -= gap

                            videojuegos[j] = temp

                        gap //= 2

                shell_sort_nombre(videojuegos)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por nombre
                def partition_nombre(videojuegos, low, high):
                    pivot = videojuegos[high].nombre
                    i = low - 1

                    for j in range(low, high):
                        if videojuegos[j].nombre < pivot:
                            i += 1
                            videojuegos[i], videojuegos[j] = videojuegos[j], videojuegos[i]

                    videojuegos[i + 1], videojuegos[high] = videojuegos[high], videojuegos[i + 1]
                    return i + 1

                def quick_sort_nombre(videojuegos, low, high):
                    if low < high:
                        pivot_index = partition_nombre(videojuegos, low, high)
                        quick_sort_nombre(videojuegos, low, pivot_index - 1)
                        quick_sort_nombre(videojuegos, pivot_index + 1, high)

                quick_sort_nombre(videojuegos, 0, len(videojuegos) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        elif criterio == "anio":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                videojuegos.sort(key=lambda videojuego: videojuego.anio)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por año
                def shell_sort_anio(videojuegos):
                    n = len(videojuegos)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = videojuegos[i]
                            j = i

                            while j >= gap and videojuegos[j - gap].anio > temp.anio:
                                videojuegos[j] = videojuegos[j - gap]
                                j -= gap

                            videojuegos[j] = temp

                        gap //= 2

                shell_sort_anio(videojuegos)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por año
                def partition_anio(videojuegos, low, high):
                    pivot = videojuegos[high].anio
                    i = low - 1

                    for j in range(low, high):
                        if videojuegos[j].anio < pivot:
                            i += 1
                            videojuegos[i], videojuegos[j] = videojuegos[j], videojuegos[i]

                    videojuegos[i + 1], videojuegos[high] = videojuegos[high], videojuegos[i + 1]
                    return i + 1

                def quick_sort_anio(videojuegos, low, high):
                    if low < high:
                        pivot_index = partition_anio(videojuegos, low, high)
                        quick_sort_anio(videojuegos, low, pivot_index - 1)
                        quick_sort_anio(videojuegos, pivot_index + 1, high)

                quick_sort_anio(videojuegos, 0, len(videojuegos) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        else:
            print("Criterio de ordenamiento inválido.")
    else:
        print("No se han ingresado videojuegos.")


def menu():
    videojuegos = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar videojuego")
        print("2. Mostrar videojuegos")
        print("3. Eliminar videojuego")
        print("4. Modificar videojuego")
        print("5. Ordenar videojuegos por nombre")
        print("6. Ordenar videojuegos por año")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de la videojuego: ")
            anio = int(input("Ingrese el año de la videojuego: "))
            videojuego = Videojuego(nombre, anio)
            videojuegos.append(videojuego)
            print("Videojuegos ingresada exitosamente.")
        elif opcion == "2":
            mostrar_videojuegos(videojuegos)
        elif opcion == "3":
            eliminar_videojuego(videojuegos)
        elif opcion == "4":
            modificar_videojuego(videojuegos)
        elif opcion == "5":
            ordenar_videojuegos(videojuegos, "nombre")
        elif opcion == "6":
            ordenar_videojuegos(videojuegos, "anio")
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()