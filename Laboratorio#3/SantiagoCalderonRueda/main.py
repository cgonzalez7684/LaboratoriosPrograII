# ############################################################
#   Santiago Calderon Rueda Laboratorio#3                    #
#   Elabore un programa tipo consola que permita ejemplificar#
# las acciones de agregar,                                   #
#   eliminar, modificar y recorrer una estructura tipo       #
# <list>, el contexto del desarrollo                         #
#   queda a criterio del estudiante                          #
##############################################################

# Vamos a definir la lista vacía
lista = []

# Función que se encarga de agregar elementos a la lista
def agregar():
    elemento = input("Ingresa el elemento a agregar: ")
    lista.append(elemento)

# Función para eliminar elementos de la lista
def eliminar():
    elemento = input("Ingresa el elemento a eliminar: ")
    if elemento in lista:
        lista.remove(elemento)
    else:
        print("El elemento no se encuentra en la lista.")

# Función para modificar elementos de la lista
def modificar():
    elemento = input("Ingresa el elemento a modificar: ")
    if elemento in lista:
        indice = lista.index(elemento)
        nuevo_elemento = input("Ingresa el nuevo elemento: ")
        lista[indice] = nuevo_elemento
    else:
        print("El elemento no se encuentra en la lista.")

# Función para recorrer la lista
def recorrer():
    print("Elementos de la lista:")
    for elemento in lista:
        print(elemento)

# Menú de opciones
while True:
    print("=== MENÚ DE OPCIONES ===")
    print("1. Agregar elemento")
    print("2. Eliminar elemento")
    print("3. Modificar elemento")
    print("4. Recorrer lista")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        agregar()
    elif opcion == "2":
        eliminar()
    elif opcion == "3":
        modificar()
    elif opcion == "4":
        recorrer()
    elif opcion == "5":
        break
    else:
        print("Opción inválida.")
