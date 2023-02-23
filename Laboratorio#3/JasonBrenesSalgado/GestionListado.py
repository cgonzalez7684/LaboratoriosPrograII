
listadoFrutas = []

def encabezadoMenu():
    print ("========Bienvenidos==========")    
    print ("Opcion #1 agregar fruta al listado : ")
    print ("Opcion #2 eliminar fruta del listado : ")
    print ("Opcion #3 modificar fruta del listado : ")
    print ("Opcion #4 imprimir el listado de frutas agregadas")
    print ("=============================")

def crearListado(frutas):    
    listadoFrutas.append (frutas)
    

def eliminarFruta(frutas):
    listadoFrutas.remove(frutas)
   

def modificarFruta(frutas , nuevafruta):  
    
    indice = listadoFrutas.index(frutas)
    listadoFrutas[indice] = nuevafruta

def imprimirLista():
        
    for n in listadoFrutas :
        print ("Lista de frutas: " , n )
        