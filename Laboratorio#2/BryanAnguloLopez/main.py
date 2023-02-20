import GestionVentas as gv
from Dominio import Factura


#Este metodo registrar facturas
def registrarfactura():
   cliente = input("¿Cual es el nombre del cliente?")
   monto = float(input("Digitar el monto de la factura: "))
   categoriav = input("Ingrese la categoria de la venta")
   
   gv.crearFactura(cliente,monto,categoriav)
    
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
    print("Esto es fuera del while") 
        

if __name__ == "__main__":
    main()
    