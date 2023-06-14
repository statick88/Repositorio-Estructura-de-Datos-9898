class Alcohol_Etilico:
    def __init__(self, nombre, anio):
        self.nombre = nombre
        self.anio = anio

    def __str__(self):
        return f"{self.nombre} ({self.anio})"

# Función para mostrar el alcohol
def mostrar_alcohol(alcohol):
    if alcohol:
        print("bebidas alcoholicas ingresadas:")
        for bebida in alcohol:
            print(bebida)
    else:
        print("No se han ingresado bebidas alcoholicas.")

# Función que elimina el producto alcohol
def eliminar_bebida(alcohol):
    if alcohol:
        nombre = input("Ingrese el nombre de la bebida alcoholica a eliminar: ")
        alcohol_filtradas = [bebida for bebida in alcohol if bebida.nombre != nombre]
        if len(alcohol_filtradas) < len(alcohol):
            alcohol[:] = alcohol_filtradas
            print("Bebida alcoholica eliminada exitosamente.")
        else:
            print("No se encontró una bebida alcoholica con ese nombre.")
    else:
        print("No se han ingresado bebidas alcoholicas.")

def modificar_bebida(alcohol):
    if alcohol:
        nombre = input("Ingrese el nombre de la bebida alcoholica a modificar: ")
        for bebida in alcohol:
            if bebida.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre de la bebida alcoholica: ")
                nuevo_anio = int(input("Ingrese el nuevo año de la bebida alcoholica: "))
                bebida.nombre = nuevo_nombre
                bebida.anio = nuevo_anio
                print("Bebida alcoholica modificada exitosamente.")
                return
        print("No se encontró una bebida alcoholica con ese nombre.")
    else:
        print("No se han ingresado bebidas alcoholicas.")

def ordenar_alcohol(alcohol, criterio):
    if alcohol:
        if criterio == "nombre":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                alcohol.sort(key=lambda bebida: bebida.nombre)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por nombre
                def shell_sort_nombre(alcohol):
                    n = len(alcohol)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = alcohol[i]
                            j = i

                            while j >= gap and alcohol[j - gap].nombre > temp.nombre:
                                alcohol[j] = alcohol[j - gap]
                                j -= gap

                            alcohol[j] = temp

                        gap //= 2

                shell_sort_nombre(alcohol)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por nombre
                def partition_nombre(alcohol, low, high):
                    pivot = alcohol[high].nombre
                    i = low - 1

                    for j in range(low, high):
                        if alcohol[j].nombre < pivot:
                            i += 1
                            alcohol[i], alcohol[j] = alcohol[j], alcohol[i]

                    alcohol[i + 1], alcohol[high] = alcohol[high], alcohol[i + 1]
                    return i + 1

                def quick_sort_nombre(alcohol, low, high):
                    if low < high:
                        pivot_index = partition_nombre(alcohol, low, high)
                        quick_sort_nombre(alcohol, low, pivot_index - 1)
                        quick_sort_nombre(alcohol, pivot_index + 1, high)

                quick_sort_nombre(alcohol, 0, len(alcohol) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        elif criterio == "anio":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                alcohol.sort(key=lambda bebida: bebida.anio)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por año
                def shell_sort_anio(alcohol):
                    n = len(alcohol)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = alcohol[i]
                            j = i

                            while j >= gap and alcohol[j - gap].anio > temp.anio:
                                alcohol[j] = alcohol[j - gap]
                                j -= gap

                            alcohol[j] = temp

                        gap //= 2

                shell_sort_anio(alcohol)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por año
                def partition_anio(alcohol, low, high):
                    pivot = alcohol[high].anio
                    i = low - 1

                    for j in range(low, high):
                        if alcohol[j].anio < pivot:
                            i += 1
                            alcohol[i], alcohol[j] = alcohol[j], alcohol[i]

                    alcohol[i + 1], alcohol[high] = alcohol[high], alcohol[i + 1]
                    return i + 1

                def quick_sort_anio(alcohol, low, high):
                    if low < high:
                        pivot_index = partition_anio(alcohol, low, high)
                        quick_sort_anio(alcohol, low, pivot_index - 1)
                        quick_sort_anio(alcohol, pivot_index + 1, high)

                quick_sort_anio(alcohol, 0, len(alcohol) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        else:
            print("Criterio de ordenamiento inválido.")
    else:
        print("No se han ingresado bebidas alcoholicas.")

def menu():
    alcohol = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar bebida alcoholica")
        print("2. Mostrar bebidas alcoholicas")
        print("3. Eliminar bebida alcoholica")
        print("4. Modificar bebida alcoholica")
        print("5. Ordenar bebidas alcoholicas por nombre")
        print("6. Ordenar bebidas alcoholicas por año")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de la bebida alcoholica: ")
            anio = int(input("Ingrese el año de la bebida alcoholica : "))
            bebida = Alcohol_Etilico(nombre, anio)
            alcohol.append(bebida)
            print("Bebida alcoholica ingresada exitosamente.")
        elif opcion == "2":
            mostrar_alcohol(alcohol)
        elif opcion == "3":
            eliminar_bebida(alcohol)
        elif opcion == "4":
            modificar_bebida(alcohol)
        elif opcion == "5":
            ordenar_alcohol(alcohol, "nombre")
        elif opcion == "6":
            ordenar_alcohol(alcohol, "anio")
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

menu()
