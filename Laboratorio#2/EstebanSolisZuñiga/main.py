import GestionVentas as gv
from Dominio import Factura


#Este metodo registrar facturas
def registrarfactura():
   nombre = input("Digitar el nombre del cliente: ")
   
   monto = float(input("Digitar el monto de la factura: "))

   gv.tiposDescuentos()

   categoria = input("Digitar la categoria del descuento que desea aplicar: ")

   gv.crearFactura(monto, categoria, nombre)
   
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
    