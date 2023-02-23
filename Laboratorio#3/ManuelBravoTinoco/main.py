lista = ["manuel", "oscar", "lunes", 2, 5, 7]

# Función para mostrar la lista
def mostrar_lista():
    print("La lista actual es:", lista)

# Función para agregar un elemento a la lista
def agregar_elemento():
    elemento = input("Ingrese el elemento que desea agregar: ")
    lista.append(elemento)
    print("Se agregó el elemento", elemento, "a la lista")

# Función para eliminar un elemento de la lista
def eliminar_elemento():
    elemento = input("Ingrese el elemento que desea eliminar: ")
    if elemento in lista:
        lista.remove(elemento)
        print("Se eliminó el elemento", elemento, "de la lista")
    else:
        print("El elemento", elemento, "no se encuentra en la lista")

# Función para modificar un elemento de la lista
def modificar_elemento():
    elemento = input("Ingrese el elemento que desea modificar: ")
    if elemento in lista:
        indice = lista.index(elemento)
        nuevo_elemento = input("Ingrese el nuevo valor para el elemento: ")
        lista[indice] = nuevo_elemento
        print("Se modificó el elemento", elemento, "por", nuevo_elemento)
    else:
        print("El elemento", elemento, "no se encuentra en la lista")

# Ciclo principal del programa
while True:
    # Mostramos el menú de opciones
    print("\n-- MENÚ --")
    print("1. Mostrar lista")
    print("2. Agregar elemento")
    print("3. Eliminar elemento")
    print("4. Modificar elemento")
    print("5. Salir")

    # Leemos la opción elegida por el usuario
    opcion = input("Ingrese una opción: ")

    # Evaluamos la opción elegida y llamamos a la función correspondiente
    if opcion == "1":
        mostrar_lista()
    elif opcion == "2":
        agregar_elemento()
    elif opcion == "3":
        eliminar_elemento()
    elif opcion == "4":
        modificar_elemento()
    elif opcion == "5":
        print("Adiós!")
        break
    else:
        print("Opción inválida, intente nuevamente")