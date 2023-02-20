import GestionVentas as gv
from Dominio import Factura


#Este metodo registrar facturas
def registrarfactura():
   cliente = str(input("Ingrese el nombre del cliente: "))
   monto = float(input("Digitar el monto de la factura: "))
   categoria_venta = str(input("Ingrese la categoria de la factura A, B O C: "))
   gv.crearFactura(monto,categoria_venta,cliente)
   
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
    