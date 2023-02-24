#Elabore un programa tipo consola que permita ejemplificar las acciones de agregar, eliminar, 
#modificar y recorrer una estructura tipo <list>, el contexto del desarrollo queda a criterio del estudiante.

# Funciones auxiliares

def imprimir_lista(lista):
    """Imprime la lista en la consola"""
    print(f"Lista actual: {lista}")

def agregar_elemento(lista, elemento):
    """Agrega un elemento a la lista"""
    lista.append(elemento)
    print(f"Elemento '{elemento}' agregado a la lista")
    imprimir_lista(lista)

def modificar_elemento(lista, posicion, nuevo_valor):
    """Modifica un elemento de la lista en una posición específica"""
    if posicion < 0 or posicion >= len(lista):
        print(f"La posición {posicion} está fuera de rango")
    else:
        lista[posicion] = nuevo_valor
        print(f"Elemento en la posición {posicion} modificado a '{nuevo_valor}'")
        imprimir_lista(lista)

def eliminar_elemento(lista, posicion):
    """Elimina un elemento de la lista en una posición específica"""
    if posicion < 0 or posicion >= len(lista):
        print(f"La posición {posicion} está fuera de rango")
    else:
        elemento = lista.pop(posicion)
        print(f"Elemento '{elemento}' eliminado de la lista")
        imprimir_lista(lista)

# Programa principal

print("Bienvenido al programa de listas")

lista = []

while True:
    opcion = input("¿Qué desea hacer? (a: agregar, m: modificar, e: eliminar, r: recorrer, s: salir) ")
    
    if opcion == "a":
        elemento = input("Escriba el elemento que desea agregar: ")
        agregar_elemento(lista, elemento)
    elif opcion == "m":
        posicion = int(input("Escriba la posición del elemento que desea modificar: "))
        nuevo_valor = input("Escriba el nuevo valor del elemento: ")
        modificar_elemento(lista, posicion, nuevo_valor)
    elif opcion == "e":
        posicion = int(input("Escriba la posición del elemento que desea eliminar: "))
        eliminar_elemento(lista, posicion)
    elif opcion == "r":
        print("Recorriendo la lista:")
        for elemento in lista:
            print(elemento)
    elif opcion == "s":
        print("Hasta luego")
        break
    else:
        print("Opción no válida, por favor intente de nuevo")