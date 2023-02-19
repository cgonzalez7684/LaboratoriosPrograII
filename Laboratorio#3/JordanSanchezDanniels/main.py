
# laboratorio_3


def lista_Jordan(lista):

    print("Lista:")

def nuevo_elemento(lista, elemento):
    lista.append(elemento)
    print("Elemento agregado a lista Jordan")
    lista(lista)

def modificar_elemento(lista, posicion, valor):

    if posicion < 0 or posicion >= len(lista):
        print("La posición no es correcta")
    else:
        lista[posicion] = valor
        print("Elemento en nueva posicion")
        lista(lista)

def eliminar_elemento(lista, posicion):

    if posicion < 0 or posicion >= len(lista):
        print("La posición no es correcta")
    else:
        elemento = lista.pop(posicion)
        print("Elemento eliminado de la lista")
        lista(lista)

print("ingresar a la lista")

lista = []

while True:
    opcion = input("digite:(A: agregar, M: modificar, E: eliminar, S: salir) ")
    
    if opcion == "A":
        elemento =input("Escriba el nuevo elemento que desea agregar: ")
        nuevo_elemento(lista, elemento)
    elif opcion == "M":
        posicion =input("Escriba la posición del elemento que desea modificar: ")
        nuevo_valor =input("Escriba el nuevo valor del elemento: ")
        modificar_elemento(lista, posicion, nuevo_valor)
    elif opcion == "E":
        posicion =input("Escriba la posición del elemento que desea eliminar: ")
        eliminar_elemento(lista, posicion)
    elif opcion == "S":
        print("SALIR")
    else:
        print("Incorrecto ingrese nuevamente")