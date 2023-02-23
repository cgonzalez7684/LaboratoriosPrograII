import GestionVentas as gv
from Dominio import Factura

def registrarfactura():
   monto = float(input("Digite la categoria de venta: "))
   gv.crearFactura(monto)
   
def imprimirfacturas():
    gv.imprimirfacturas()
    

    
def main(): 
       
    while True:
        gv.encabezadoSistema()
        opcion = int(input("Digite la categoria de venta: "))
        if (opcion == 1):
            registrarfactura()
        elif (opcion == 2):  
            registrarfactura()        
        elif (opcion == 3):  
            registrarfactura()        
        else: 
            continue
    
        

if __name__ == "__main__":
    main()
    