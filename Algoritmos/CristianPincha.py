class Licor:
    def __init__(self, nombre, grados_alcohol):
        self.nombre = nombre
        self.grados_alcohol = grados_alcohol

    def __str__(self):
        return f"{self.nombre} ({self.grados_alcohol} grados)"


def mostrar_licores(licores):
    if licores:
        print("Licores ingresados:")
        for licor in licores:
            print(licor)
    else:
        print("No se han ingresado licores.")


def eliminar_licor(licores):
    if licores:
        nombre = input("Ingrese el nombre del licor a eliminar: ")
        licores_filtrados = [licor for licor in licores if licor.nombre != nombre]
        if len(licores_filtrados) < len(licores):
            licores[:] = licores_filtrados
            print("Licor eliminado exitosamente.")
        else:
            print("No se encontró un licor con ese nombre.")
    else:
        print("No se han ingresado licores.")


def modificar_licor(licores):
    if licores:
        nombre = input("Ingrese el nombre del licor a modificar: ")
        for licor in licores:
            if licor.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre del licor: ")
                nuevos_grados = float(input("Ingrese los nuevos grados de alcohol del licor: "))
                licor.nombre = nuevo_nombre
                licor.grados_alcohol = nuevos_grados
                print("Licor modificado exitosamente.")
                return
        print("No se encontró un licor con ese nombre.")
    else:
        print("No se han ingresado licores.")


def ordenar_licores(licores, criterio):
    if licores:
        if criterio == "nombre":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                licores.sort(key=lambda licor: licor.nombre)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por nombre
                def shell_sort_nombre(licores):
                    n = len(licores)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = licores[i]
                            j = i

                            while j >= gap and licores[j - gap].nombre > temp.nombre:
                                licores[j] = licores[j - gap]
                                j -= gap

                            licores[j] = temp

                        gap //= 2

                shell_sort_nombre(licores)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por nombre
                def partition_nombre(licores, low, high):
                    pivot = licores[high].nombre
                    i = low - 1

                    for j in range(low, high):
                        if licores[j].nombre < pivot:
                            i += 1
                            licores[i], licores[j] = licores[j], licores[i]

                    licores[i + 1], licores[high] = licores[i + 1]
                    return i + 1


                def quick_sort_nombre(licores, low, high):
                    if low < high:
                        pivot_index = partition_nombre(licores, low, high)
                        quick_sort_nombre(licores, low, pivot_index - 1)
                        quick_sort_nombre(licores, pivot_index + 1, high)

                quick_sort_nombre(licores, 0, len(licores) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        elif criterio == "grados":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                licores.sort(key=lambda licor: licor.grados_alcohol)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por grados
                def shell_sort_grados(licores):
                    n = len(licores)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = licores[i]
                            j = i

                            while j >= gap and licores[j - gap].grados_alcohol > temp.grados_alcohol:
                                licores[j] = licores[j - gap]
                                j -= gap

                            licores[j] = temp

                        gap //= 2

                shell_sort_grados(licores)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por grados
                def partition_grados(licores, low, high):
                    pivot = licores[high].grados_alcohol
                    i = low - 1

                    for j in range(low, high):
                        if licores[j].grados_alcohol < pivot:
                            i += 1
                            licores[i], licores[j] = licores[j], licores[i]

                    licores[i + 1], licores[high] = licores[high], licores[i + 1]
                    return i + 1

                def quick_sort_grados(licores, low, high):
                    if low < high:
                        pivot_index = partition_grados(licores, low, high)
                        quick_sort_grados(licores, low, pivot_index - 1)
                        quick_sort_grados(licores, pivot_index + 1, high)

                quick_sort_grados(licores, 0, len(licores) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        else:
            print("Criterio de ordenamiento inválido.")
    else:
        print("No se han ingresado licores.")


def menu():
    licores = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar licor")
        print("2. Mostrar licores")
        print("3. Eliminar licor")
        print("4. Modificar licor")
        print("5. Ordenar licores por nombre")
        print("6. Ordenar licores por grados de alcohol")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del licor: ")
            grados_alcohol = float(input("Ingrese los grados de alcohol del licor: "))
            licor = Licor(nombre, grados_alcohol)
            licores.append(licor)
            print("Licor ingresado exitosamente.")
        elif opcion == "2":
            mostrar_licores(licores)
        elif opcion == "3":
            eliminar_licor(licores)
        elif opcion == "4":
            modificar_licor(licores)
        elif opcion == "5":
            ordenar_licores(licores, "nombre")
        elif opcion == "6":
            ordenar_licores(licores, "grados")
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
                print("Opción inválida. Por favor, ingrese una opción válida.")

                
menu()
