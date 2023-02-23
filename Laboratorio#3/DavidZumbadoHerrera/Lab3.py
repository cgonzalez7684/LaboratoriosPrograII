

mylist = [25,16,89,45,10,60]

def main(): 
       
    while True:
        print("1. Agregar un valor a la lista")
        print("2. Modificar un valor de la lista")
        print("3. Mostrar la cantidad de datos de la lista")
        print("4. Eliminar un valor de la lista")
        opcion = int(input("Digitar la opción sistema: "))
        if (opcion == 1):
            Agregar()
        elif (opcion == 2):
            Modificar()
        elif (opcion == 3):
            Recorrido()  
        elif (opcion == 4):
            Eliminar()  
        else:
            continue

def Agregar():

    print("La lista de numeros es: ", mylist)
    numero = int(input("Agregue un nuevo numero: "))
    mylist.append(numero)
    print("La lista de numeros es: ", mylist)

def Modificar():
    print("La lista de numeros es: ", mylist)
    numeroactual = int(input("Indique la posicion del numero que desea cambiar: ")) #seleccione el indice del dato
    nuevonumero = int(input("Indique el nuevo numero: "))
    mylist[numeroactual] = nuevonumero
    print("La lista de numeros es: ", mylist)

def Eliminar():
    print("1. Eliminar un valor de la lista")
    print("2. Eliminar todos los valores de la lista")
    opcion = int(input("Digitar la opción sistema: "))

    if  (opcion == 1):
            print("La lista de numeros es: ", mylist)
            numero = int(input("Ingrese el numero que desea eliminar: "))
            mylist.remove(numero)
            print("La lista de numeros es: ", mylist)
    elif    (opcion == 2):
            print("La lista de numeros es: ", mylist)
            mylist.clear()
            print("La lista de numeros es: ", mylist)
    else:
        main()  

def Recorrido():
    print("La cantidad de datos en la lista es: ", len(mylist))

if __name__ == "__main__":
    main()