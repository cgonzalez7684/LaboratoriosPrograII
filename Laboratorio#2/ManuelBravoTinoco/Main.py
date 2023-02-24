import GestionVentas as gv
from Dominio import Factura
21

#Este metodo registrar facturas
def registrarfactura():
   monto = float(input("Digitar el monto de la factura: "))
   categoria = input("Digitar la categoría de la venta (A, B o C): ")
   nombre = input("Digitar el nombre del cliente: ")
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
    print("Esto es fuera del while") 
        

if __name__ == "__main__":
    main()