# Función para mostrar el menú de opciones
def mostrar_menu():
    print("Qué acción desea realizar en la lista?")
    print("1. Agregar un elemento")
    print("2. Eliminar un elemento")
    print("3. Modificar un elemento")
    print("4. Recorrer la lista")
    print("5. Salir")

# Lista inicial
lista = []

# Ciclo principal del programa
while True:
    # Mostrar el menú de opciones
    mostrar_menu()

    # Pedir al usuario que seleccione una opción
    opcion = input("Digite el número de la opción a elegir: ")

    # Agregar un elemento
    if opcion == "1":
        elemento = input("Introduce el elemento a agregar: ")
        lista.append(elemento)
        print(f"El elemento '{elemento}' ha sido agregado a la lista.")

    # Eliminar un elemento
    elif opcion == "2":
        if len(lista) == 0:
            print("La lista está vacía, no se puede eliminar ningún elemento.")
        else:
            indice = int(input("Introduce el índice del elemento a eliminar: "))
            if indice < 0 or indice >= len(lista):
                print("Índice inválido, por favor introduce un índice válido.")
            else:
                elemento_eliminado = lista.pop(indice)
                print(f"El elemento '{elemento_eliminado}' ha sido eliminado de la lista.")

    # Modificar un elemento
    elif opcion == "3":
        if len(lista) == 0:
            print("La lista está vacía, no se puede modificar ningún elemento.")
        else:
            indice = int(input("Introduce el índice del elemento a modificar: "))
            if indice < 0 or indice >= len(lista):
                print("Índice inválido, por favor introduce un índice válido.")
            else:
                nuevo_elemento = input("Introduce el nuevo elemento: ")
                lista[indice] = nuevo_elemento
                print(f"El elemento en el índice {indice} ha sido modificado.")

    # Recorrer la lista
    elif opcion == "4":
        print("La lista actual es la siguiente:")
        for elemento in lista:
            print(elemento)

    # Salir del programa
    elif opcion == "5":
        print("Saliendo del programa...")
        break

    # Opción inválida
    else:
        print("Opción inválida, por favor selecciona una opción válida.")