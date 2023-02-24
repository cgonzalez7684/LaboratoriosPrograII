import GestionVentas as gv
from Dominio import Factura


#Este metodo registrar facturas
def registrarfactura():
    monto = float(input("Digitar el monto de la factura: "))
    categoria = input("Cual es la categoria del descuento?(A,B,C): ") # 
    nombre = input("Cual es el nombre del cliente? ")
    gv.crearFactura(monto,categoria,nombre)
   
def imprimirfacturas():
    gv.imprimirfacturas()
    

    
def main(): 
       
    while True:
        gv.encabezadoSistema()
        opcion = int(input("Digitar la opción sistema: "))
        if (opcion == 1):
            registrarfactura()
        elif (opcion == 2):  #y sino si
            imprimirfacturas()        
        else: #y sino
            continue
    print("Digite una opcion valida") 
        

if __name__ == "__main__":
    main()
    