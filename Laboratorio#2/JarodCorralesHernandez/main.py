import GestionVentas as gv
from Dominio import Factura

def registrarfactura():
   monto = float(input("Por favor digite el monto de la factura: "))
   categoria = input("Por favor inserte la categoria de venta ya sea A, B o C: ")
   gv.crearFactura(monto, categoria)
   
def imprimirfacturas():
    gv.imprimirfacturas()
    

    
def main(): 
       
    while True:
        gv.encabezadoSistema()
        opcion = int(input("Por favor digite la opcion que le corresponda: "))
        if (opcion == 1):
            registrarfactura()
        elif (opcion == 2):  
            imprimirfacturas()               
        else: 
            continue
    
        

if __name__ == "__main__":
    main()
    