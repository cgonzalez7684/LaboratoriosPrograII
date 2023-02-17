import GestionVentas as gv
from Dominio import Factura

def categoriaVenta():
   categoria = float(input("Digite la categoria: "))
   gv.crearFactura(categoria)

def registrarfactura():
   monto = float(input("Digitar el monto de la factura: "))
   gv.crearFactura(monto)
   
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
    
        

if __name__ == "__main__":
    main()             