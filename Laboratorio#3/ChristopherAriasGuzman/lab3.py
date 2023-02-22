lista = []

def agregar_Nombre():
    Nombre = input("Ingrese un Nombre para agregar a la lista: ")
    lista.append(Nombre)
    print(f"El Nombre '{Nombre}' se agregó correctamente a la lista")

def eliminar_Nombre():
    Nombre = input("Ingrese un Nombre para eliminar de la lista: ")
    if Nombre in lista:
        lista.remove(Nombre)
        print(f"El Nombre '{Nombre}' se eliminó correctamente de la lista")
    else:
        print(f"El Nombre '{Nombre}' no se encontró en la lista")

def modificar_Nombre():
    Nombre_viejo = input("Ingrese el Nombre a modificar: ")
    Nombre_nuevo = input("Ingrese el nuevo valor para el Nombre: ")
    if Nombre_viejo in lista:
        indice = lista.index(Nombre_viejo)
        lista[indice] = Nombre_nuevo
        print(f"El Nombre '{Nombre_viejo}' se modificó correctamente a '{Nombre_nuevo}'")
    else:
        print(f"El Nombre '{Nombre_viejo}' no se encontró en la lista")

def recorrer_lista():
    print("Los Nombres de la lista son:")
    for Nombre in lista:
        print(f"- {Nombre}")

while True:
    print("\n--- Programa para manejar nombres de una lista ---")
    print("1. Agregar un Nombre")
    print("2. Eliminar un Nombre")
    print("3. Modificar un Nombre")
    print("4. Recorrer la lista")
    print("5. Salir")
    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        agregar_Nombre()
    elif opcion == "2":
        eliminar_Nombre()
    elif opcion == "3":
        modificar_Nombre()
    elif opcion == "4":
        recorrer_lista()
    elif opcion == "5":
        print("Gracias por tu preferencia :)!!")
        break
    else:
        print("Opción inválida")