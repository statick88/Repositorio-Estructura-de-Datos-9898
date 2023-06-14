class Libro:
    def __init__(self, Obra, publicacion):
        self.Obra = Obra
        self.publicacion = publicacion

    def __str__(self):
        return f"{self.Obra} ({self.publicacion})"


def mostrar_libro(libros):
    if libros:
        print("Libros ingresados:")
        for libro in libros:
            print(libro)
    else:
        print("No se han ingresado Libros.")


def eliminar_libro(libros):
    if libros:
        Obra = input("Ingrese el  nombre de la Obra a eliminar: ")
        peliculas_filtradas = [libro for libro in libros if libro.Obra != Obra]
        if len(peliculas_filtradas) < len(libros):
            libros[:] = peliculas_filtradas
            print("Libro eliminado exitosamente.")
        else:
            print("No se encontró una libro con ese Obra.")
    else:
        print("No se han ingresado Libros.")



def modificar_libro(libros):
    if libros:
        Obra = input("Ingrese el nombre de la  Obra del libro a modificar: ")
        for libro in libros:
            if libro.Obra == Obra:
                nuevo_nombre = input("Ingrese el nuevo nombre de la Obra del libro: ")
                nuevo_anio = int(input("Ingrese el nuevo año de la libro: "))
                libro.Obra = nuevo_nombre
                libro.publicacion = nuevo_anio
                print("Libro modificada exitosamente.")
                return
        print("No se encontró una libro con ese Obra.")
    else:
        print("No se han ingresado Libros.")


def ordenar_libros(libros, criterio):
    if libros:
        if criterio == "Obra":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                libros.sort(key=lambda libro: libro.Obra)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por Obra
                def shell_sort_nombre(libros):
                    n = len(libros)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = libros[i]
                            j = i

                            while j >= gap and libros[j - gap].Obra > temp.Obra:
                                libros[j] = libros[j - gap]
                                j -= gap

                            libros[j] = temp

                        gap //= 2

                shell_sort_nombre(libros)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por Obra
                def partition_nombre(libros, low, high):
                    pivot = libros[high].Obra
                    i = low - 1

                    for j in range(low, high):
                        if libros[j].Obra < pivot:
                            i += 1
                            libros[i], libros[j] = libros[j], libros[i]

                    libros[i + 1], libros[high] = libros[high], libros[i + 1]
                    return i + 1

                def quick_sort_nombre(libros, low, high):
                    if low < high:
                        pivot_index = partition_nombre(libros, low, high)
                        quick_sort_nombre(libros, low, pivot_index - 1)
                        quick_sort_nombre(libros, pivot_index + 1, high)

                quick_sort_nombre(libros, 0, len(libros) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        elif criterio == "publicacion":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                libros.sort(key=lambda libro: libro.publicacion)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por año
                def shell_sort_anio(libros):
                    n = len(libros)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = libros[i]
                            j = i

                            while j >= gap and libros[j - gap].publicacion > temp.publicacion:
                                libros[j] = libros[j - gap]
                                j -= gap

                            libros[j] = temp

                        gap //= 2

                shell_sort_anio(libros)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por año
                def partition_anio(libros, low, high):
                    pivot = libros[high].publicacion
                    i = low - 1

                    for j in range(low, high):
                        if libros[j].publicacion < pivot:
                            i += 1
                            libros[i], libros[j] = libros[j], libros[i]

                    libros[i + 1], libros[high] = libros[high], libros[i + 1]
                    return i + 1

                def quick_sort_anio(libros, low, high):
                    if low < high:
                        pivot_index = partition_anio(libros, low, high)
                        quick_sort_anio(libros, low, pivot_index - 1)
                        quick_sort_anio(libros, pivot_index + 1, high)

                quick_sort_anio(libros, 0, len(libros) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        else:
            print("Criterio de ordenamiento inválido.")
    else:
        print("No se han ingresado Libros.")


def menu():
    libros = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar libro")
        print("2. Mostrar Libros")
        print("3. Eliminar libro")
        print("4. Modificar libro")
        print("5. Ordenar Libros por Obra")
        print("6. Ordenar Libros por año")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            Obra = input("Ingrese el nombre de la Obra del libro: ")
            publicacion = int(input("Ingrese el año de publicacion del libro: "))
            libro = Libro(Obra, publicacion)
            libros.append(libro)
            print("Libro ingresado exitosamente.")
        elif opcion == "2":
            mostrar_libro(libros)
        elif opcion == "3":
            eliminar_libro(libros)
        elif opcion == "4":
            modificar_libro(libros)
        elif opcion == "5":
            ordenar_libros(libros, "Obra")
        elif opcion == "6":
            ordenar_libros(libros, "publicacion")
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()