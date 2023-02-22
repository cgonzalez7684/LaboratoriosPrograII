import GestionVentas as gv
from Dominio import Factura


#Este metodo registrar facturas
def registrarfactura():
   monto = float(input("Digitar el monto de la factura: "))
   categoriaVenta = input("Cual es la categoria del descuento?")
   if (categoriaVenta=="C" or "c"):
            descuento = input("Ingrese el monto seleccionado para el descuento: ")
   cliente = input("Cual es el nombre del cliente?")
   gv.crearFactura(monto,categoriaVenta,  cliente)
   
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
    