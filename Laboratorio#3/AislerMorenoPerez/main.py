#Aqui creamos una nueva lista+
lista = []

#Aqui agregamos elementos a la lista
def agregarElemento():
    numero = int(input("Digita un numero: "))
    lista.append(numero)

#Aqui eliminamos elementos de la lista
def eliminarElementos():
    numero = int(input("Digita el numero que desea eliminar: "))
    lista.remove(numero)

#Aqui modificamos el elemento de la lista
def modificarElementos():
    numero = int(input("Digita el numero que desea modificar: "))
    index = lista.index(numero)
    lista[index] =int(input("Digita el nuevo numero que quiere reemplazar: "))
#Imprimimos nuestra lista
def imprimirLista():
 print("Los numeros de la lista son:", lista)


def Logica():
    while True:
        print("")
        print("1) Agregar un nuevo numero")
        print("2) Eliminar un numero")
        print("3) Modificar un numero")
        print("4) Imprimir lista")
        print("5) Salir")
        print("")
        opcion = int(input("Digitar la opción sistema: "))

        if(opcion == 1):
            agregarElemento()
        elif(opcion == 2):
            eliminarElementos()
        elif(opcion == 3):
            modificarElementos()
        elif(opcion == 4):
            imprimirLista()
        elif(opcion == 5):
            break
        
def main(): 
       
    Logica()
        

if __name__ == "__main__":
    main()