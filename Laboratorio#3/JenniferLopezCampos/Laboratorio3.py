def manejarLista():
    lista = []
    while True:
  
        print("Seleccione una opción: ")
        print("1. Agregar numero")
        print("2. Eliminar numero")
        print("3. Modificar numero")
        print("4. Recorrer lista")
        print("5. Salir")
        opcion = int(input("Opción seleccionada: "))

        if opcion == 1:
            elemento = input("Ingrese el numero que desea agregar: ")
            lista.append(elemento)
            print("Numero agregado correctamente")
        elif opcion == 2:
            if len(lista) == 0:
                print("La lista está vacía")
            else:
                indice = int(input("Ingrese el índice del numero que desea eliminar (0 a {}): ".format(len(lista)-1)))
                if indice < 0 or indice >= len(lista):
                    print("Índice inválido")
                else:
                    del lista[indice]
                    print("Numero eliminado correctamente")
        elif opcion == 3:
            if len(lista) == 0:
                print("La lista está vacía")
            else:
                indice = int(input("Ingrese el índice del numero que desea modificar (0 a {}): ".format(len(lista)-1)))
                if indice < 0 or indice >= len(lista):
                    print("Índice inválido")
                else:
                    nuevo_elemento = input("Ingrese el nuevo numero: ")
                    lista[indice] = nuevo_elemento
                    print("Numero modificado correctamente")
        elif opcion == 4:
            if len(lista) == 0:
                print("La lista está vacía")
            else:
                print("Numeros en la lista:")
                for i, elemento in enumerate(lista):
                    print("{}: {}".format(i, elemento))
        elif opcion == 5:
            break
        else:
            print("Opción inválida")

    print("Salir")
    
manejarLista()