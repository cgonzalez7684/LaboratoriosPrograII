#Elabore un programa tipo consola que permita ejemplificar las acciones de agregar, eliminar, 
#modificar y recorrer una estructura tipo <list>, el contexto del desarrollo queda a criterio del estudiante.

#Funciones auxiliares 


def main():
    numeros = input("Ingrese una lista de números separados por comas: ")
    lista = [int(num) for num in numeros.split(",")]
    print("Lista original:", lista)

    while True:
        print("\n¿Qué acción desea realizar?")
        print("1. Agregar un número a la lista")
        print("2. Eliminar un número de la lista")
        print("3. Modificar un número de la lista")
        print("4. Recorrer la lista")
        print("5. Salir del programa")

        opcion = input("Ingrese el número correspondiente a la acción que desea realizar: ")

        if opcion == "1":
            numero = int(input("Ingrese el número que desea agregar a la lista: "))
            lista.append(numero)
            print("Lista actualizada:", lista)
        elif opcion == "2":
            numero = int(input("Ingrese el número que desea eliminar de la lista: "))
            if numero in lista:
                lista.remove(numero)
                print("Lista actualizada:", lista)
            else:
                print("El número que ingresó no se encuentra en la lista.")
        elif opcion == "3":
            numero_viejo = int(input("Ingrese el número que desea modificar en la lista: "))
            if numero_viejo in lista:
                indice = lista.index(numero_viejo)
                numero_nuevo = int(input("Ingrese el nuevo número: "))
                lista[indice] = numero_nuevo
                print("Lista actualizada:", lista)
            else:
                print("El número que ingresó no se encuentra en la lista.")
        elif opcion == "4":
            print("Recorriendo la lista...")
            for numero in lista:
                print(numero)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("La opción ingresada no es válida. Por favor, ingrese un número del 1 al 5.")
            