import GestionVentas as gv
from Dominio import Factura


#Este metodo registrar facturas
def registrarfactura():
   montofactura = float(input("Digitar el montofacturade la factura: "))
   categoria = str(input("Seleccione la categoria del descuento: "))
   gv.crearFactura(montofactura,categoria)
   
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
    