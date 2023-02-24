lista = []

while True:
    # Mostrar el menú de opciones
    print("\n--- Menú de opciones ---")
    print("1. Agregar elementos")
    print("2. Eliminar elementos")
    print("3. Modificar elementos")
    print("4. Recorrer la lista")
    print("5. Salir del programa")

    # Pedir al usuario que seleccione una opción
    opcion = int(input("\nSeleccione una opción: "))

    if opcion == 1:
        # Agregar elementos a la lista
        cantidad = int(input("Ingrese la cantidad de elementos que desea agregar: "))
        for i in range(cantidad):
            elemento = input(f"Ingrese el elemento {i+1}: ")
            lista.append(elemento)
        print("Elementos agregados exitosamente.")

    elif opcion == 2:
        # Eliminar elementos de la lista
        if len(lista) == 0:
            print("La lista está vacía.")
        else:
            print("Elementos en la lista:")
            for i, elemento in enumerate(lista):
                print(f"{i+1}. {elemento}")
            indice = int(input("Ingrese el índice del elemento que desea eliminar: "))
            if indice < 1 or indice > len(lista):
                print("Índice inválido.")
            else:
                lista.pop(indice-1)
                print("Elemento eliminado exitosamente.")

    elif opcion == 3:
        # Modificar elementos de la lista
        if len(lista) == 0:
            print("La lista está vacía.")
        else:
            print("Elementos en la lista:")
            for i, elemento in enumerate(lista):
                print(f"{i+1}. {elemento}")
            indice = int(input("Ingrese el índice del elemento que desea modificar: "))
            if indice < 1 or indice > len(lista):
                print("Índice inválido.")
            else:
                nuevo_elemento = input("Ingrese el nuevo elemento: ")
                lista[indice-1] = nuevo_elemento
                print("Elemento modificado exitosamente.")

    elif opcion == 4:
        # Recorrer la lista
        if len(lista) == 0:
            print("La lista está vacía.")
        else:
            print("Elementos en la lista:")
            for i, elemento in enumerate(lista):
                print(f"{i+1}. {elemento}")

    elif opcion == 5:
        # Salir del programa
        print("Saliendo del programa...")
        break

    else:
        # Opción inválida
        print("Opción inválida.")