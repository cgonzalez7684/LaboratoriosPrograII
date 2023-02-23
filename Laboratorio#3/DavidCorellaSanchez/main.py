# Laboratorio 3 David Corella Sanchez
lista = []
opcion = None
def main():
    while(True):
        print("---------------------------------")
        print("1- Agregar elemento a la lista")
        print("2- Modificar elemento a la lista")
        print("3- Eliminar elemento de la lista")
        print("4- Mostrar datos de la lista")
        print("5- Salir")
        print("---------------------------------")
        opcion = input("Digite una opcion: ")
        if 1 == int(opcion):
            agregar()
        elif 2 == int(opcion):
            modificar()
        elif 3 == int(opcion):
            eliminar()
        elif 4 == int(opcion):
            mostrar()
        elif 5 == int(opcion):
            exit()
        else:
            continue
    
def agregar():
    lista.append(input("Ingrese el valor a agregar: "))
    print()
    
def modificar():
    try:
        lista[int(input("Ingrese la posicion del dato: "))] = input("Ingrese el dato: ")
        print()
    except IndexError: 
        print()
        print("El indice no existe")
    
def eliminar():
    try:
        del lista[int(input("Ingrese la posicion a eliminar: "))]
        print()
    except IndexError: 
        print()
        print("El indice no existe")

def mostrar():
    for dato in lista:
        print(str(dato))
    print()
        
if __name__ == "__main__":
    main()