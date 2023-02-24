list=[]

def agregarC():
    list.append(str(input("Escriba un nuevo color: ")))

def eliminarC():
    color = str(input("Escriba el color que desea eliminar: "))
    list.remove(color)

def modificarC():
    color = str(input("Escriba el color que desea modificar: "))
    index = list.index(color)
    list[index] =str(input("Escriba el nuevo color: "))

def listaC():
 print("Los colores agregados son:", list)

def lista():
    while True:
        print("1. Agregar un nuevo color")
        print("2. Eliminar un color")
        print("3. Modificar un color")
        print("4. Ver lista de colores")
        print("5. Salir del sistema")
        opcion = int(input("Seleccione una opción"))

        if(opcion=="1"):
            agregarC()
        elif(opcion=="2"):
            eliminarC()
        elif(opcion=="3"):
            modificarC()
        elif(opcion=="4"):
            listaC()
        elif(opcion=="5"):
            break