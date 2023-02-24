def mostrar_lista(lista):
    print("Lista completa:")
    for elemento in lista:
        print(elemento)

# Crear una lista vacía
numeros = []

while True:
    # Mostrar el menú de opciones
    print("Seleccione una opción:")
    print("1. Agregar un número")
    print("2. Modificar un número")
    print("3. Eliminar un número")
    print("4. Mostrar la lista completa")
    print("5. Salir")

    # Leer la opción seleccionada
    opcion = int(input())

    if opcion == 1:
        # Leer el nuevo número y agregarlo a la lista
        nuevo_numero = int(input("Ingrese el nuevo número: "))
        numeros.append(nuevo_numero)
    elif opcion == 2:
        if len(numeros) == 0:
            # No se puede modificar una lista vacía
            print("La lista está vacía, no se puede modificar ningún número.")
        else:
            # Leer la posición y el nuevo valor del número a modificar y modificarlo
            posicion = int(input("Ingrese la posición del número a modificar (1 - {}): ".format(len(numeros))))
            nuevo_valor = int(input("Ingrese el nuevo valor para el número: "))
            numeros[posicion - 1] = nuevo_valor
    elif opcion == 3:
        if len(numeros) == 0:
            # No se puede eliminar de una lista vacía
            print("La lista está vacía, no se puede eliminar ningún número.")
        else:
            # Leer la posición del número a eliminar y eliminarlo
            posicion = int(input("Ingrese la posición del número a eliminar (1 - {}): ".format(len(numeros))))
            numeros.pop(posicion - 1)
    elif opcion == 4:
        # Mostrar la lista completa
        mostrar_lista(numeros)
    elif opcion == 5:
        # Salir del programa
        break
    else:
        # Opción inválida
        print("Opción inválida, por favor seleccione otra.")