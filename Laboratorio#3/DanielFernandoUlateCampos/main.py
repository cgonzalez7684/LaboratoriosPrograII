list = ["Cantidad de Equipos en Stock"]

#Añadir datos en la lista
print ("Los valores de la lista son los siguientes: \n", list)
valora = input("\nColoque el valor que desea añadir")
list.append(valora)
print("La siguiente lista muestra el valor añadido\n", list)

#Eliminar datos de la lista
print("Los valores de la lista son los siguientes: \n", list)
valorb = input("\nColoque el valor que desea eliminar")
list.remove(valorb)
print("La siguiente lista muestra el valor eliminado\n", list)

#Modificar datos de la lista
print("Los valores de la lista son los siguientes: \n", list)
valorc = input("\nColoque el dato que desea modificar")
posi = list.index(valorc)
valord = input("Coloque el siguiente valor a modificar")
list[posi] = valord
print("Su lista con las modificaciones realizadas es la siguiente \n", list)


     
    while True:
         print ("----------------------------------")
         print ("Primer : Agregar dato a la lista ")
         print ("Segundo : Eliminar dato de la lista")
         print ("Tercero : Modificar dato de la lista ")
         print ("Cuarto : Ver la lista completa")
         print ("Quinto : Salir del sistema")
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
