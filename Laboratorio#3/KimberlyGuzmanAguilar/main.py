#Elabore un programa tipo consola que permita ejemplificar las acciones de agregar, eliminar, modificar y 
# recorrer una estructura tipo <list>, el contexto del desarrollo queda a criterio del estudiante.

def modificar_lista():
    listaanimales = []
    while True:
        #Opciones dentro del menu
        print("Eliga una opcion:")
        print("----------------------------------") 
        print("1. Agregar animal a la lista")
        print("2. Eliminar animal de la lista")
        print("3. Modificar lista de animales")
        print("4. Recorrer lista de animales")
        print("5. Ordenar animales dentro de la lista")
        print("6. Salir")
        print("----------------------------------") 
        opcion = int(input("Opcion seleccionada: "))
        
        if opcion == 1:
            animal = input("Anote el animal que desea agregar a la lista: ")
            listaanimales.append(animal)
            print("Animal agregado correctamente a la lista de animales :D")
        elif opcion == 2:
            if len(listaanimales) == 0:
                print("La lista de animales no contiene ningun animal D: ")
            else:
                indice = int(input("Ingrese el animal que desea eliminar (0 a {}): ".format(len(listaanimales)-1)))
                if indice < 0 or indice >= len(listaanimales):
                    print("Indice invalido")
                else:
                    del listaanimales[indice]
                    print("Animal eliminado de la lista correctamente")
        elif opcion == 3:
            if len(listaanimales) == 0:
                print("La lista de animales no contiene ningun animal D: ")
            else:
                indice = int(input("Ingrese el índice del animal a modificar (0 a {}): ".format(len(listaanimales)-1)))
                if indice < 0 or indice >= len(listaanimales):
                    print("Indice invalido")
                else:
                    nuevo_animal = input("Ingrese el nuevo animal: ")
                    listaanimales[indice] = nuevo_animal
                    print("Lista de animales modificada correctamente")

        elif opcion == 4:
            if len(listaanimales) == 0:
                print("La lista de animales no contiene ningun animal D: ")
            else:
                print("Animales contenidos en la lista de animales:")
                for i, animal in enumerate(listaanimales):
                    print("{}: {}".format(i, animal))

        elif opcion == 5:
            if len(listaanimales) == 0:
                print("La lista de animales no contiene ningun animal D: ")
            else:
                print("Lista de animales ordenadas:")
                listaanimales.sort()
                print(listaanimales)

        elif opcion == 6:
            break
        else:
            print("Opción invalida")
    
    modificar_lista()