carros = []

def ingresar():
    x = input("Digite el vehiculo: ")
    carros.append(x)

def cambiar():
    x = input("Digite el vehiculo a cambiar: ")
    if x in carros:
        i = carros.index(x)
        nuevo = input("Digite nuevo vehiculo a ingresar: ")
        carros[i] = nuevo
    else:
        print("No se encuentra")

def eliminar():
    x = input("Ingresa el vehiculo a eliminar :")
    if x in carros:
        carros.remove(x)
    else:
        print("El vehiculo no esta en lista.")

def leer_lista():
    print("Vehiculos en la lista: ")
    for x in carros:
        print(x)

while True:
    print("Ociones")
    print("Digite 1 para ingresar un vehiculo")
    print("Digite 2 para cambiar un vehiculo")
    print("Digite 3 para eliminar un vehiculo")
    print("Digite 4 para ver la lista")

    seleccion = input("Digite una opcion: ")

    if seleccion == "1":
        ingresar()
    elif seleccion == "2":
        cambiar()
    elif seleccion == "3":
        eliminar()
    elif seleccion == "4":
        leer_lista()
