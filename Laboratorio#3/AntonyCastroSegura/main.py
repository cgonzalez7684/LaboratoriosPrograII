
Lista= ["Costa Rica","España","Peru"]
    
def main(): 
       
    while True:
        encabezadoSistema()
        opcion = int(input("Digitar la opción sistema: "))
        if (opcion == 1):
            agregar()
        elif (opcion == 2):  #y sino si
            eleminar() 
        elif (opcion == 3):  #y sino si
            modificar() 
        elif (opcion == 4):  #y sino si
            recorrer()        
        else: #y sino
            continue
    print("Esto es fuera del while") 
try:
    def encabezadoSistema():
        print("----------------------------------")   
        print("Opción #1 : Agregar pais")
        print("Opción #2 : Eliminar pais")
        print("Opción #3 : Modificar pais")
        print("Opción #4 : Recorrer Lista")
        print("----------------------------------")
except BaseException:
        print('Existe un error ')
         
def agregar(valor):
    Lista.append(valor)

def recorrer():
    for n in Lista:
        print ("La lista es:", Lista)

def agregar():
    print ("Digite el pais que desea agregar: ")
    pais = input()
    Lista.append(pais)
   

def eleminar():
    op=int(input("Digite la posicion del pais que desea elminar: "))
    del Lista[op]

def modificar():
    
    ele=int(input("Digite la posicion del pais que desea modificar: "))
    n=input("Digite la modificacion del pais: ")
    Lista [ele]=n
    


        

if __name__ == "__main__":
    main()