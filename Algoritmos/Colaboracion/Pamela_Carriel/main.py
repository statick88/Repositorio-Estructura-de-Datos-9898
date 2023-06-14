class Libro:
    def __init__(self, autor, anio_public):
        self.autor = autor
        self.anio_public = anio_public

    def __str__(self):
        return f"{self.autor} ({self.anio_public})"


def mostrar_libros(Libros):
    if Libros:
        print("Libros ingresados:")
        for libro in Libros:
            print(libro)
    else:
        print("No se han ingresado libros.")


def eliminar_libro(Libros):
    if Libros:
        autor = input("Ingrese el autor del libro a eliminar: ")
        Libros_filtrados = [libro for libro in Libros if libro.autor != autor]
        if len(Libros_filtrados) < len(Libros):
            Libros[:] = Libros_filtrados
            print("Libro se ha eliminado exitosamente.")
        else:
            print("No se encontró un libro con ese autor.")
    else:
        print("No se han ingresado libros.")


def modificar_libro(Libros):
    if Libros:
        autor = input("Ingrese el autor del libro a modificar: ")
        for libro in Libros:
            if libro.autor == autor:
                nuevo_autor = input("Ingrese el nuevo autor del libro: ")
                nuevo_anio_public = int(input("Ingrese el nuevo año de publicación del libro: "))
                libro.autor = nuevo_autor
                libro.anio_public = nuevo_anio_public
                print("Libro se ha modificado exitosamente.")
                return
        print("No se encontró el libro con ese autor.")
    else:
        print("No se han ingresado libros.")


def ordenar_libros(Libros, criterio):
    if Libros:
        if criterio == "autor":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                Libros.sort(key=lambda libro: libro.autor)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por autor
                def shell_sort_autor(Libros):
                    n = len(Libros)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = Libros[i]
                            j = i

                            while j >= gap and Libros[j - gap].autor > temp.autor:
                                Libros[j] = Libros[j - gap]
                                j -= gap

                            Libros[j] = temp

                        gap //= 2

                shell_sort_autor(Libros)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por autor
                def partition_autor(Libros, low, high):
                    pivot = Libros[high].autor
                    i = low - 1

                    for j in range(low, high):
                        if Libros[j].autor < pivot:
                            i += 1
                            Libros[i], Libros[j] = Libros[j], Libros[i]

                    Libros[i + 1], Libros[high] = Libros[high], Libros[i + 1]
                    return i + 1

                def quick_sort_autor(Libros, low, high):
                    if low < high:
                        pivot_index = partition_autor(Libros, low, high)
                        quick_sort_autor(Libros, low, pivot_index - 1)
                        quick_sort_autor(Libros, pivot_index + 1, high)

                quick_sort_autor(Libros, 0, len(Libros) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        elif criterio == "anio_public":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                Libros.sort(key=lambda libro: libro.anio_public)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por año
                def shell_sort_anio_public(Libros):
                    n = len(Libros)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = Libros[i]
                            j = i

                            while j >= gap and Libros[j - gap].anio_public > temp.anio_public:
                                Libros[j] = Libros[j - gap]
                                j -= gap

                            Libros[j] = temp

                        gap //= 2

                shell_sort_anio_public(Libros)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por año
                def partition_anio_public(Libros, low, high):
                    pivot = Libros[high].anio_public
                    i = low - 1

                    for j in range(low, high):
                        if Libros[j].anio_public < pivot:
                            i += 1
                            Libros[i], Libros[j] = Libros[j], Libros[i]

                    Libros[i + 1], Libros[high] = Libros[high], Libros[i + 1]
                    return i + 1

                def quick_sort_anio_public(Libros, low, high):
                    if low < high:
                        pivot_index = partition_anio_public(Libros, low, high)
                        quick_sort_anio_public(Libros, low, pivot_index - 1)
                        quick_sort_anio_public(Libros, pivot_index + 1, high)

                quick_sort_anio_public(Libros, 0, len(Libros) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        else:
            print("Criterio de ordenamiento inválido.")
    else:
        print("No se han ingresado libros.")


def menu():
    Libros = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar libro")
        print("2. Mostrar libros")
        print("3. Eliminar libro")
        print("4. Modificar libro")
        print("5. Ordenar libros por autor")
        print("6. Ordenar libros por año")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            autor = input("Ingrese el autor del libro: ")
            anio_public = int(input("Ingrese el año de publicación del libro: "))
            libro = Libro(autor, anio_public)
            Libros.append(libro)
            print("Libro ingresado exitosamente.")
        elif opcion == "2":
            mostrar_libros(Libros)
        elif opcion == "3":
            eliminar_libro(Libros)
        elif opcion == "4":
            modificar_libro(Libros)
        elif opcion == "5":
            ordenar_libros(Libros, "autor")
        elif opcion == "6":
            ordenar_libros(Libros, "anio_public")
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()
