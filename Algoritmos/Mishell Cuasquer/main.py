class Postres:
    def __init__(self, nombre, anio):
        self.nombre = nombre
        self.anio = anio

    def __str__(self):
        return f"{self.nombre} ({self.anio})"


def mostrar_postres(postres):
    if postres:
        print("Postres ingresadas:")
        for postres in postres:
            print(postres)
    else:
        print("No se han ingresado postres.")


def eliminar_postres(postres):
    if postres:
        nombre = input("Ingrese el nombre del postre a eliminar: ")
        postres_f = [postres for postres in postres  if postres.nombre != nombre]
        if len(postres_f) < len(postres):
            postres[:] = postres_f
            print("Postre eliminado exitosamente.")
        else:
            print("No se encontró un postre  con ese nombre.")
    else:
        print("No se han ingresado postres.")



def modificar_postres(postres):
    if postres:
        nombre = input("Ingrese el nombre del postre a modificar: ")
        for postres in postres:
            if postres.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre de la película: ")
                nuevo_anio = int(input("Ingrese el nuevo año de la película: "))
                postres.nombre = nuevo_nombre
                postres.anio = nuevo_anio
                print("Película modificada exitosamente.")
                return
        print("No se encontró una película con ese nombre.")
    else:
        print("No se han ingresado películas.")


def ordenar_postres(postres, criterio):
    if postres:
        if criterio == "nombre":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                postres.sort(key=lambda postres: postres.nombre)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por nombre
                def shell_sort_nombre(postres):
                    n = len(postres)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = postres[i]
                            j = i

                            while j >= gap and postres[j - gap].nombre > temp.nombre:
                                postres[j] = postres[j - gap]
                                j -= gap

                            postres[j] = temp

                        gap //= 2

                shell_sort_nombre(postres)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por nombre
                def partition_nombre(postres, low, high):
                    pivot = postres[high].nombre
                    i = low - 1

                    for j in range(low, high):
                        if postres[j].nombre < pivot:
                            i += 1
                            postres[i], postres[j] = postres[j], postres[i]

                    postres[i + 1], postres[high] = postres[high], postres[i + 1]
                    return i + 1

                def quick_sort_nombre(postres, low, high):
                    if low < high:
                        pivot_index = partition_nombre(postres, low, high)
                        quick_sort_nombre(postres, low, pivot_index - 1)
                        quick_sort_nombre(postres, pivot_index + 1, high)

                quick_sort_nombre(postres, 0, len(postres) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        elif criterio == "anio":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                postres.sort(key=lambda postres: postres.anio)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por año
                def shell_sort_anio(postres):
                    n = len(postres)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = postres[i]
                            j = i

                            while j >= gap and postres[j - gap].anio > temp.anio:
                                postres[j] = postres[j - gap]
                                j -= gap

                            postres[j] = temp

                        gap //= 2

                shell_sort_anio(postres)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por año
                def partition_anio(postres, low, high):
                    pivot = postres[high].anio
                    i = low - 1

                    for j in range(low, high):
                        if postres[j].anio < pivot:
                            i += 1
                            postres[i], postres[j] = postres[j], postres[i]

                    postres[i + 1], postres[high] = postres[high], postres[i + 1]
                    return i + 1

                def quick_sort_anio(postres, low, high):
                    if low < high:
                        pivot_index = partition_anio(postres, low, high)
                        quick_sort_anio(postres, low, pivot_index - 1)
                        quick_sort_anio(postres, pivot_index + 1, high)

                quick_sort_anio(postres, 0, len(postres) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        else:
            print("Criterio de ordenamiento inválido.")
    else:
        print("No se han ingresado películas.")


def menu():
    postres = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar postre")
        print("2. Mostrar postre")
        print("3. Eliminar postre")
        print("4. Modificar postre")
        print("5. Ordenar postres por nombre")
        print("6. Ordenar postres por año")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del postre: ")
            anio = int(input("Ingrese el año del postre: "))
            postres = postres(nombre, anio)
            postres.append(postres)
            print("Película ingresada exitosamente.")
        elif opcion == "2":
            mostrar_postres(postres)
        elif opcion == "3":
            eliminar_postres(postres)
        elif opcion == "4":
            modificar_postres(postres)
        elif opcion == "5":
            ordenar_postres(postres, "nombre")
        elif opcion == "6":
            ordenar_postres(postres, "anio")
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()