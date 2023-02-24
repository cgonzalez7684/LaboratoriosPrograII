
listaHelados = ["Rico Ice", "Dulce Tropic", "Oasis", "Planeta Cream", "Polo"]

print("---Heladería de Helados---\n")

while True:
    print("\nMenú de Opciones")
    print("1) Desplegar Helados")
    print("2) Añadir Helados")
    print("3) Eliminar Helados")
    print("4) Modificar Helados")
    print("5) Salir")
    opc = int(input("\nSeleccione una opción: \n"))

    if opc == 1:
        print("\n>>>Nuestros Helados<<<")
        for i in listaHelados:
            print(i)
    elif opc == 2:
        listaHelados.append(input("Digite el Helado a Añadir: "))
        print("Helado Añadido")
    elif opc == 3:
        listaHelados.remove(input("Digite el Helado a Eliminar: "))
        print("Helado eliminado")
    elif opc == 4:
        indice = listaHelados.index(input("¿Cuál Helado desea modificar?: "))
        listaHelados[indice] = input("Ingrese el nuevo Helado: ")
        print("Helado modificado con éxito!")
    elif opc == 5:
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida. Seleccione una opción válida.")
