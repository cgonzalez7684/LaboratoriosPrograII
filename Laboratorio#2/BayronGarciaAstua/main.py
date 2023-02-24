import GestionVentas as gv
from Dominio import Factura


#Este metodo registrar facturas
def registrarfactura():
   monto = float(input("Digitar el monto de la factura: "))
   print("Digite la categoría de la factura")
   print("Cat 'A' para un 5% de descuento ")
   print("Cat 'B' para un 10% de descuento ")
   print("Cat 'C' para un descuento personalizado ")
   categoriaVenta = input("Categoria: ")
   gv.crearFactura(monto, categoriaVenta)
   
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
    