class Pelicula:
    def __init__(self, nombre, anio):
        self.nombre = nombre
        self.anio = anio

    def __str__(self):
        return f"{self.nombre} ({self.anio})"


def mostrar_animales(animales):
    if animales:
        print("Películas ingresadas:")
        for animal in animales:
            print(animal)
    else:
        print("No se han ingresado películas.")

def eliminar_animal(animales):
    if animales:
        nombre = input("Ingrese el nombre de la película a eliminar: ")
        animales_filtradas = [animal for animal in animales if animal.nombre != nombre]
        if len(animales_filtradas) < len(animales):
            animales[:] = animales_filtradas
            print("Animal eliminada exitosamente.")
        else:
            print("No se encontró un animal con ese nombre.")
    else:
        print("No se han ingresado animales.")



def modificar_animales(animales):
    if animales:
        nombre = input("Ingrese el nombre de la película a modificar: ")
        for animal in animales:
            if animal.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre de el animal: ")
                nuevo_anio = int(input("Ingrese el nuevo año de el animal: "))
                pelicula.nombre = nuevo_nombre
                pelicula.anio = nuevo_anio
                print("Animal modificada exitosamente.")
                return
        print("No se encontró un animal con ese nombre.")
    else:
        print("No se han ingresado animales.")


def ordenar_animales(animales, criterio):
    if animales:
        if criterio == "nombre":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                animales.sort(key=lambda pelicula: pelicula.nombre)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por nombre
                def shell_sort_nombre(animales):
                    n = len(animales)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = animales[i]
                            j = i

                            while j >= gap and animales[j - gap].nombre > temp.nombre:
                                animales[j] = animales[j - gap]
                                j -= gap

                            animales[j] = temp

                        gap //= 2

                shell_sort_nombre(animales)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por nombre
                def partition_nombre(animales, low, high):
                    pivot = animales[high].nombre
                    i = low - 1

                    for j in range(low, high):
                        if animales[j].nombre < pivot:
                            i += 1
                            animales[i], animales[j] = animales[j], animales[i]

                    animales[i + 1], animales[high] = animales[high], animales[i + 1]
                    return i + 1

                def quick_sort_nombre(animales, low, high):
                    if low < high:
                        pivot_index = partition_nombre(animales, low, high)
                        quick_sort_nombre(animales, low, pivot_index - 1)
                        quick_sort_nombre(animales, pivot_index + 1, high)

                quick_sort_nombre(animales, 0, len(animales) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        elif criterio == "anio":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                animales.sort(key=lambda animal: animal.anio)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por año
                def shell_sort_anio(animales):
                    n = len(animales)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp =animales[i]
                            j = i

                            while j >= gap and animales[j - gap].anio > temp.anio:
                                animales[j] = animales[j - gap]
                                j -= gap

                            animales[j] = temp

                        gap //= 2

                shell_sort_anio(animales)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por año
                def partition_anio(animales, low, high):
                    pivot = animales[high].anio
                    i = low - 1

                    for j in range(low, high):
                        if animales[j].anio < pivot:
                            i += 1
                            animales[i], animales[j] = animales[j], animales[i]

                    animales[i + 1], animales[high] = animales[high], animales[i + 1]
                    return i + 1

                def quick_sort_anio(animales, low, high):
                    if low < high:
                        pivot_index = partition_anio(animales, low, high)
                        quick_sort_anio(animales, low, pivot_index - 1)
                        quick_sort_anio(animales, pivot_index + 1, high)

                quick_sort_anio(animales, 0, len(animales) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        else:
            print("Criterio de ordenamiento inválido.")
    else:
        print("No se han ingresado películas.")


def menu():
    animales = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar animal")
        print("2. Mostrar animales")
        print("3. Eliminar animal")
        print("4. Modificar animal")
        print("5. Ordenar animales por nombre")
        print("6. Ordenar animales por año")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de  el animal: ")
            anio = int(input("Ingrese el año de el animal: "))
            animal = animales(nombre, anio)
            animal.append(animal)
            print("Película ingresada exitosamente.")
        elif opcion == "2":
            mostrar_animales(animales)
        elif opcion == "3":
            eliminar_animal(animales)
        elif opcion == "4":
            modificar_animales(animales)
        elif opcion == "5":
            ordenar_animales(animales, "nombre")
        elif opcion == "6":
            ordenar_animales(animales, "anio")
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()