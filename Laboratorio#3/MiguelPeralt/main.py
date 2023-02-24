# Definimos la lista inicial
lista = []

# Función para agregar un elemento a la lista
def agregar_elemento():
    elemento = input("Ingresa el elemento que deseas añadir': ")
    lista.append(elemento)

# Función para eliminar un elemento de la lista
def eliminar_elemento():
    if len(lista) == 0:
        print("La lista está vacía, no hay elementos para borrar")
    else:
        elemento = input("Ingresa el elemento que deseas borrar: ")
        if elemento in lista:
            lista.remove(elemento)

# Función para modificar un elemento de la lista
def modificar_elemento():
    
    index = input("Ingresa el elemento que deseas modificar: ")
    elemento_nuevo = input("Ingresa el nuevo valor para el elemento: ")
    lista[index] = elemento_nuevo


# Función para recorrer la lista y mostrar sus elementos
def recorrer_lista():
    if len(lista) == 0:
        print("La lista está vacía")
    else:
        print("Los elementos de la lista son:")
        for elemento in lista:
            print("- " + elemento)

# Menú principal del programa
while True:
    print("Qué acción deseas realizar: ")
    print("1. Agregar un elemento a la lista: ")
    print("2. Eliminar un elemento de la lista: ")
    print("3. Modificar un elemento de la lista: ")
    print("4. Recorrer la lista: ")
    print("5. Salir del programa: ")
    opcion = input("Ingresa el número de la opción que deseas: ")

    if opcion == "1":
        agregar_elemento()
    elif opcion == "2":
        eliminar_elemento()
    elif opcion == "3":
        modificar_elemento()
    elif opcion == "4":
        recorrer_lista()
    elif opcion == "5":
        print("Finalizando programa")
        break
    else:
        print("Opción inválida, intenta de nuevo")
