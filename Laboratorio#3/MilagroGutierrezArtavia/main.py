lista = ["Inglés", "Álgebra", "Programación"]
opcion = None

#menú de opciones
def main():
  while True:
      opcion = int(input("\nMenú: \n 1. Agregar nuevas asignaturas \n 2. Eliminar asignaturas \n 3. Modificar asignaturas \n 4. Mostrar asignaturas \n 5. Salir del menú de opciones\n Elija una opción: "))
      if opcion == 1:
          agregar_asignatura()
      elif opcion == 2:
        eliminar_asignatura()
      elif opcion == 3:
        modificar_asignatura()
      elif opcion == 4:
        mostrar_lista()
      elif opcion == 5:
        salir_menu()
      else:
        print("\nLa opción es incorrecta")
      continue 
   
   #funciones 
def agregar_asignatura():
    posicion = None
    letra = input("\nSi desea agregar la asignatura al final de la lista digite la letra n, \nsi desea agregar la asignatura en una posición específica digite la letra i: ")
    print()
    if letra == "i":
        posicion = int(input("Digite el índice: "))
        if posicion < 0 or posicion >= len(lista):
            print("La posición digitada está fuera de rango")
        else:
            lista.insert(posicion, input("Ingrese una nueva asignatura: "))
            print("La lista con la nueva asignatura es: ", lista)
    elif letra == "n":
        lista.append(input("Ingrese una nueva asignatura: "))
        print("La lista con la nueva asignatura es: ", lista)
    else:
        print("La letra es incorrecta")
        
    
def eliminar_asignatura():
    posicion = int(input("\nDigite la posición que desea eliminar: "))
    if posicion < 0 or posicion >= len(lista):
        print("El índice está fuera del rango")
    else:
        eliminada = lista.pop(posicion)
        print(f"Asignatura '{eliminada}' eliminada de la lista")
        print("\nLista actualizada: ", lista)
    
def modificar_asignatura():
    posicion = int(input("\nDigite la posición que desea modificar: "))
    if posicion < 0 or posicion >= len(lista):
        print(f"La posición {posicion} está fuera de rango")
    else:
        reemplazo = input("\nDigite la nueva asignatura: ")
        lista[posicion] = reemplazo
        print(f"La asignatura en la posición {posicion} se ha modificado a:'{reemplazo}'")
        print("\nLista actualizada: ", lista)
    
def mostrar_lista():
    print("\nLa lista es:")
    for n in lista:
        print(n)
    
def salir_menu():
    print("\n¡Gracias por usar el menú!\n")
    exit()
    
if __name__ == "__main__":
    main()