class Mascotas:
    def __init__(self, nombre, anio):
        self.nombre = nombre
        self.anio = anio

    def __str__(self):
        return f"{self.nombre} ({self.anio})"


def mostrar_mascotas(mascotas):
    if mascotas:
        print("Mascotas ingresadas:")
        for mascota in mascotas:
            print(mascota)
    else:
        print("No se han ingresado mascotas.")


def eliminar_mascotas(mascotas):
    if mascotas:
        nombre = input("Ingrese el nombre de la mascota a eliminar: ")
        mascotas_filtradas = [mascota for mascota in mascotas if mascota.nombre != nombre]
        if len(mascotas_filtradas) < len(mascotas):
            mascotas[:] = mascotas_filtradas
            print("Mascota eliminada exitosamente.")
        else:
            print("No se encontró una mascota con ese nombre.")
    else:
        print("No se han ingresado mascotas.")


def modificar_mascota(mascotas):
    if mascotas:
        nombre = input("Ingrese el nombre de la mascota a modificar: ")
        for mascota in mascotas:
            if mascota.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre de la mascota: ")
                nuevo_anio = int(input("Ingrese el nuevo año de la mascota: "))
                mascota.nombre = nuevo_nombre
                mascota.anio = nuevo_anio
                print("Mascota modificada exitosamente.")
                return
        print("No se encontró una mascota con ese nombre.")
    else:
        print("No se han ingresado mascotas.")


def ordenar_mascotas(mascotas, criterio):
    if mascotas:
        if criterio == "nombre":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                mascotas.sort(key=lambda mascota: mascota.nombre)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por nombre
                def shell_sort_nombre(mascotas):
                    n = len(mascotas)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = mascotas[i]
                            j = i

                            while j >= gap and mascotas[j - gap].nombre > temp.nombre:
                                mascotas[j] = mascotas[j - gap]
                                j -= gap

                            mascotas[j] = temp

                        gap //= 2

                shell_sort_nombre(mascotas)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por nombre
                def partition_nombre(mascotas, low, high):
                    pivot = mascotas[high].nombre
                    i = low - 1

                    for j in range(low, high):
                        if mascotas[j].nombre < pivot:
                            i += 1
                            mascotas[i], mascotas[j] = mascotas[j], mascotas[i]

                    mascotas[i + 1], mascotas[high] = mascotas[high], mascotas[i + 1]
                    return i + 1

                def quick_sort_nombre(mascotas, low, high):
                    if low < high:
                        pivot_index = partition_nombre(mascotas, low, high)
                        quick_sort_nombre(mascotas, low, pivot_index - 1)
                        quick_sort_nombre(mascotas, pivot_index + 1, high)

                quick_sort_nombre(mascotas, 0, len(mascotas) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        elif criterio == "anio":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                mascotas.sort(key=lambda mascota: mascota.anio)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por año
                def shell_sort_anio(mascotas):
                    n = len(mascotas)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = mascotas[i]
                            j = i

                            while j >= gap and mascotas[j - gap].anio > temp.anio:
                                mascotas[j] = mascotas[j - gap]
                                j -= gap

                            mascotas[j] = temp

                        gap //= 2

                shell_sort_anio(mascotas)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por año
                def partition_anio(mascotas, low, high):
                    pivot = mascotas[high].anio
                    i = low - 1

                    for j in range(low, high):
                        if mascotas[j].anio < pivot:
                            i += 1
                            mascotas[i], mascotas[j] = mascotas[j], mascotas[i]

                    mascotas[i + 1], mascotas[high] = mascotas[high], mascotas[i + 1]
                    return i + 1

                def quick_sort_anio(mascotas, low, high):
                    if low < high:
                        pivot_index = partition_anio(mascotas, low, high)
                        quick_sort_anio(mascotas, low, pivot_index - 1)
                        quick_sort_anio(mascotas, pivot_index + 1, high)

                quick_sort_anio(mascotas, 0, len(mascotas) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        else:
            print("Criterio de ordenamiento inválido.")
    else:
        print("No se han ingresado mascotas.")


def menu():
    mascotas = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar mascota")
        print("2. Mostrar mascotas")
        print("3. Eliminar mascota")
        print("4. Modificar mascota")
        print("5. Ordenar mascotas por nombre")
        print("6. Ordenar mascotas por año")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de la mascota: ")
            anio = int(input("Ingrese el año de la mascota: "))
            mascota = Mascotas(nombre, anio)
            mascotas.append(mascota)
            print("Mascota ingresada exitosamente.")
        elif opcion == "2":
            mostrar_mascotas(mascotas)
        elif opcion == "3":
            eliminar_mascotas(mascotas)
        elif opcion == "4":
            modificar_mascota(mascotas)
        elif opcion == "5":
            ordenar_mascotas(mascotas, "nombre")
        elif opcion == "6":
            ordenar_mascotas(mascotas, "anio")
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()
