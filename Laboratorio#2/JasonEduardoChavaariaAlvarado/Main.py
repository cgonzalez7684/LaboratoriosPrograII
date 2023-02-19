import SalesManagment as gv
from Domain import Factura



def registrarfactura():
   monto = float(input("Ingresar el monto de la factura: "))
   gv.crearFactura(monto)
   
def imprimirfacturas():
    gv.imprimirfacturas()
    

    
def main(): 
       
    while True:
        gv.encabezadoSistema()
        opcion = int(input("Ingresar la opción del sistema: "))
        if (opcion == 1):
            registrarfactura()
        elif (opcion == 2):  #y sino si
            imprimirfacturas()        
        else: #y sino
            continue
    print("Factura") 
        

if __name__ == "__main__":
    main()