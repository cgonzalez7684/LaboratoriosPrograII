"""
Enunciado del laboratorio#3

Elabore un programa tipo consola que permita ejemplificar las acciones de agregar, 
eliminar, modificar y recorrer una estructura tipo <list>, el contexto del desarrollo 
queda a criterio del estudiante.

Hecho por Warren Bonilla Jiménez
Programación II
UIA

"""

lista = [] #creacion de lista


def agregar():
    print("Los datos de su lista son: \n",lista)
    datoa = input("\nDigite un dato para agregar a la lista: ")
    lista.append(datoa)
    print("Su nueva lista con el dato agregado es: \n", lista)
    return

def eliminar():
    print("Los datos de su lista son: \n",lista)
    datoe = input("\nDigite un dato para eliminarlo de la lista: ")
    lista.remove(datoe)
    print("Su nueva lista con el dato eliminado es: \n", lista)
    return

def modificar():
    print("Los datos de su lista son: \n",lista)
    datom = input("\nDigite el dato de los anteriores que le gustaria modificar de la lista: ")
    posi = lista.index(datom) #se obtiene la posicion del dato a modificar
    datom2 = input("\nDigite el nuevo dato a modificar: ") # se obtiene el nuevo dato a modificar
    lista[posi] = datom2
    print("Su nueva lista modificada es: \n",lista)
    return

def verlista():
    print("\nLos datos de su lista son: \n",lista)
    return

def menu():
   
     
    while True:
         print ("----------------------------------")
         print ("Opción #1 : Agregar dato a la lista ")
         print ("Opción #2 : Eliminar dato de la lista")
         print ("Opción #3 : Modificar dato de la lista ")
         print ("Opción #4 : Ver la lista completa")
         print ("Opción #5 : Salir del sistema")
         print ("==================================")
         opcion = input("Digite una opción del sistema: ")
         
         if(opcion =="1"):
            agregar()
         elif (opcion =="2"):
            eliminar()
         elif (opcion =="3"):
            modificar()
         elif (opcion =="4"):
            verlista()
         elif (opcion == "5"):
            print("\n¡Hasta luego!")
            break 
         else:
            print("Opcion denegada\n Intente de nuevo")
            continue
       
    
menu()


