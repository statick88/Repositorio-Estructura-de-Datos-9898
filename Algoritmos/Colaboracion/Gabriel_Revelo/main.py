class PlatoDeComida:
    def _init_(self, nombre, anio):
        self.nombre = nombre
        self.anio = anio

    def _str_(self):
        return f"{self.nombre} ({self.anio})"


def mostrar_platos(platos):
    if platos:
        print("Platos de comida ingresados:")
        for plato in platos:
            print(plato)
    else:
        print("No se han ingresado platos de comida.")


def eliminar_plato(platos):
    if platos:
        nombre = input("Ingrese el nombre del plato de comida a eliminar: ")
        platos_filtrados = [plato for plato in platos if plato.nombre != nombre]
        if len(platos_filtrados) < len(platos):
            platos[:] = platos_filtrados
            print("Plato de comida eliminado exitosamente.")
        else:
            print("No se encontró un plato de comida con ese nombre.")
    else:
        print("No se han ingresado platos de comida.")


def modificar_plato(platos):
    if platos:
        nombre = input("Ingrese el nombre del plato de comida a modificar: ")
        for plato in platos:
            if plato.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre del plato de comida: ")
                nuevo_anio = int(input("Ingrese el nuevo año del plato de comida: "))
                plato.nombre = nuevo_nombre
                plato.anio = nuevo_anio
                print("Plato de comida modificado exitosamente.")
                return
        print("No se encontró un plato de comida con ese nombre.")
    else:
        print("No se han ingresado platos de comida.")


def ordenar_platos(platos, criterio):
    if platos:
        if criterio == "nombre":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                platos.sort(key=lambda plato: plato.nombre)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por nombre
                def shell_sort_nombre(platos):
                    n = len(platos)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = platos[i]
                            j = i

                            while j >= gap and platos[j - gap].nombre > temp.nombre:
                                platos[j] = platos[j - gap]
                                j -= gap

                            platos[j] = temp

                        gap //= 2

                shell_sort_nombre(platos)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por nombre
                def partition_nombre(platos, low, high):
                    pivot = platos[high].nombre
                    i = low - 1

                    for j in range(low, high):
                        if platos[j].nombre < pivot:
                            i += 1
                            platos[i], platos[j] = platos[j], platos[i]

                    platos[i + 1], platos[high] = platos[high], platos[i + 1]
                    return i + 1

                def quick_sort_nombre(platos, low, high):
                    if low < high:
                        pivot_index = partition_nombre(platos, low, high)
                        quick_sort_nombre(platos, low, pivot_index - 1)
                        quick_sort_nombre(platos, pivot_index + 1, high)

                quick_sort_nombre(platos, 0, len(platos) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        elif criterio == "anio":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                platos.sort(key=lambda plato: plato.anio)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por año
                def shell_sort_anio(platos):
                    n = len(platos)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = platos[i]
                            j = i

                            while j >= gap and platos[j - gap].anio > temp.anio:
                                platos[j] = platos[j - gap]
                                j -= gap

                            platos[j] = temp

                        gap //= 2

                shell_sort_anio(platos)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por año
                def partition_anio(platos, low, high):
                    pivot = platos[high].anio
                    i = low - 1

                    for j in range(low, high):
                        if platos[j].anio < pivot:
                            i += 1
                            platos[i], platos[j] = platos[j], platos[i]

                    platos[i + 1], platos[high] = platos[high], platos[i + 1]
                    return i + 1

                def quick_sort_anio(platos, low, high):
                    if low < high:
                        pivot_index = partition_anio(platos, low, high)
                        quick_sort_anio(platos, low, pivot_index - 1)
                        quick_sort_anio(platos, pivot_index + 1, high)

                quick_sort_anio(platos, 0, len(platos) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        else:
            print("Criterio de ordenamiento inválido.")
    else:
        print("No se han ingresado platos de comida.")


def menu():
    platos = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar plato de comida")
        print("2. Mostrar platos de comida")
        print("3. Eliminar plato de comida")
        print("4. Modificar plato de comida")
        print("5. Ordenar platos de comida por nombre")
        print("6. Ordenar platos de comida por año")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del plato de comida: ")
            anio = int(input("Ingrese el año del plato de comida: "))
            plato = PlatoDeComida(nombre, anio)
            platos.append(plato)
            print("Plato de comida ingresado exitosamente.")
        elif opcion == "2":
            mostrar_platos(platos)
        elif opcion == "3":
            eliminar_plato(platos)
        elif opcion == "4":
            modificar_plato(platos)
        elif opcion == "5":
            ordenar_platos(platos, "nombre")
        elif opcion == "6":
            ordenar_platos(platos, "anio")
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()