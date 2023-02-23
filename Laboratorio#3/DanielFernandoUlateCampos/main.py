lista = [] #Crea la lista

def agregar():
   print("Los valores de su lista son: \n", lista)
   valora = input("\nDigite el valor que desea agregar a la lista: ")
   lista.append(valora)
   print("Su lista actualizada es: \n", lista)
   return

def eliminar():
   print("Los valores de su lista son: \n", lista)
   valorb = input("\nDigite el valor que desea eliminar de la lista: ")
   lista.remove(valorb)
   print("Su lista actualizada es: \n", lista)
   return

def modificar():
   print("Los valores de su lista son: \n", lista)
   valorc = input("\nDigite el valor de la lista que desea modificar: ")
   posi = lista.index(valorc)
   valord = input ("\nDigite el nuevo valor que desea modificar")
   lista[posi] = valord
   print("Su lista actualizada es: \n", lista)
   return

def verlista():
   print("\nLos valores de su lista son: \n", lista)
   return

def menu():
   
   while True:
       print ("-----------------------------------------------")
       print ("Alternativa#1 : Agregar el dato a la lista")
       print ("Alternativa#2 : Eliminar el dato de la lista")
       print ("Alternativa#3 : Modificar el dato de la lista")
       print ("Alternativa#4 : Ver lista COmpleta")
       print ("Alternativa#5 : Salir del Sistema")
       print ("================================================")
       alternativa = input("Digite una alternativa del sistema: ")
       
       if(alternativa =="1"):
          agregar()
       elif(alternativa =="2"):
         eliminar()
       elif(alternativa =="3"):
         modificar()
       elif(alternativa =="4"):
          verlista()
       elif(alternativa =="5"):
         print("\nNos vemos en la próxima")
         continue
      
menu()

       
