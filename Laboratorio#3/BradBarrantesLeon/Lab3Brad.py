#BradBarrantesLeon#

#Lab 3#

#Elabore un programa tipo consola que permita ejemplificar las acciones de agregar, eliminar, modificar y#
#recorrer una estructura tipo <list>, el contexto del desarrollo queda a criterio del estudiante.#

while True:
    
    print("Pagina Principal")
    print("1) Desplegar")
    print("2) Añadir")
    print("3) Eliminar")
    print("4) Modificar")
    print("5) Salir")

    opc = int(input("Seleccione una opción:"))
    if opc == 1:
        print(">>>Productos<<<")
        for m in lista:
            print(m)
    elif opc == 2:
        lista.append(input("Producto para agregar: "))
        print("Añadido")
    elif opc == 3:
        lista.remove(input("Producto para Eliminar: "))
        print("Eliminado")
    elif opc == 4:
        indice = lista.index(input("¿Que desea modificar?: "))
        lista[indice] = input("Ingresar: ")
        print("Modificacion completada!")
    elif opc == 5:
        print("salir")
        break
    else:
        print("Opción inválida. Seleccione una opcion valida.")