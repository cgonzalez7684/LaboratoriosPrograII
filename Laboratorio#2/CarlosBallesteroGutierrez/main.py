import GestionVentas as gv
from Dominio import Factura


#Este metodo registrar facturas
def registrarfactura():
   nombreCliente =str(input("Digite nombre del cliete: "))
   monto = float(input("Digitar el monto de la factura: "))
   categoriaventa = str(input("Digite la gategoria de la factura (A, B ó C): "))
   gv.crearFactura(monto,categoriaventa,nombreCliente)
   
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
    