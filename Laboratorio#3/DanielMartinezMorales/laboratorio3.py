
lista = []


def agregar_elemento():
    elemento = input("Ingrese el elemento que desea agregar: ")
    lista.append(elemento)
    print("El elemento se ha agregado correctamente a la lista")


def eliminar_elemento():
    elemento = input("Ingrese el elemento que desea eliminar: ")
    if elemento in lista:
        lista.remove(elemento)
        print("El elemento se ha eliminado correctamente de la lista")
    else:
        print("El elemento no se encuentra en la lista")


def modificar_elemento():
    elemento = input("Ingrese el elemento que desea modificar: ")
    if elemento in lista:
        nuevo_elemento = input("Ingrese el nuevo elemento: ")
        indice = lista.index(elemento)
        lista[indice] = nuevo_elemento
        print("El elemento se ha modificado correctamente")
    else:
        print("El elemento no se encuentra en la lista")


def recorrer_lista():
    print("Los elementos de la lista son:")
    for elemento in lista:
        print(elemento)


while True:
    print("\nMENU DE OPCIONES")
    print("1. Agregar elemento a la lista")
    print("2. Eliminar elemento de la lista")
    print("3. Modificar elemento de la lista")
    print("4. Recorrer lista")
    print("5. Salir")

    opcion = int(input("Ingrese la opción que desea ejecutar: "))

    if opcion == 1:
        agregar_elemento()
    elif opcion == 2:
        eliminar_elemento()
    elif opcion == 3:
        modificar_elemento()
    elif opcion == 4:
        recorrer_lista()
    elif opcion == 5:
        print("Gracias por utilizar el programa")
        break
    else:
        print("Opción inválida, intente nuevamente")
