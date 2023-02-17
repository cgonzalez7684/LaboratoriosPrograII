#Anthony Enrique Alvarez Delgado
#Laboratorio 3
#Elabore un programa tipo consola que permita ejemplificar las acciones de agregar, eliminar, modificar y
#recorrer una estructura tipo <list>, el contexto del desarrollo queda a criterio del estudiante.

def manejar_lista():
    lista = []
    while True:
        # Imprimir menú de opciones
        print("Seleccione una opción:")
        print("1. Agregar elemento")
        print("2. Eliminar elemento")
        print("3. Modificar elemento")
        print("4. Recorrer lista")
        print("5. Salir")
        opcion = int(input("Opción seleccionada: "))

        # Realizar acción dependiendo de la opción seleccionada
        if opcion == 1:
            elemento = input("Ingrese el elemento a agregar: ")
            lista.append(elemento)
            print("Elemento agregado correctamente")
        elif opcion == 2:
            if len(lista) == 0:
                print("La lista está vacía")
            else:
                indice = int(input("Ingrese el índice del elemento a eliminar (0 a {}): ".format(len(lista)-1)))
                if indice < 0 or indice >= len(lista):
                    print("Índice inválido")
                else:
                    del lista[indice]
                    print("Elemento eliminado correctamente")
        elif opcion == 3:
            if len(lista) == 0:
                print("La lista está vacía")
            else:
                indice = int(input("Ingrese el índice del elemento a modificar (0 a {}): ".format(len(lista)-1)))
                if indice < 0 or indice >= len(lista):
                    print("Índice inválido")
                else:
                    nuevo_elemento = input("Ingrese el nuevo elemento: ")
                    lista[indice] = nuevo_elemento
                    print("Elemento modificado correctamente")
        elif opcion == 4:
            if len(lista) == 0:
                print("La lista está vacía")
            else:
                print("Elementos en la lista:")
                for i, elemento in enumerate(lista):
                    print("{}: {}".format(i, elemento))
        elif opcion == 5:
            break
        else:
            print("Opción inválida")

    print("Saliendo de la función")
    
manejar_lista()