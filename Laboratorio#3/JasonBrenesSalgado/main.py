import GestionListado as gl


def main():
    
    while True:
        gl.encabezadoMenu()
        
        opcion = int(input("Digite una opción del sistema: "))
        if(opcion == 1):
            nombrefruta = input("Nombre de la fruta que desea agregar : ")
            gl.crearListado(nombrefruta)
        elif (opcion == 2 ):
            nombrefruta = input("Nombre la fruta que desea eliminar : ")
            gl.eliminarFruta(nombrefruta)
        elif (opcion == 3 ):
            nombrefruta = input("Nombre de la fruta que desea modificar : ")
            nuevafruta = input ("Agregue el nombre de la nueva fruta : ")
            gl.modificarFruta(nombrefruta,nuevafruta)
        elif (opcion == 4):
            gl.imprimirLista()
        else:
            continue


if __name__=="__main__":
    main()
