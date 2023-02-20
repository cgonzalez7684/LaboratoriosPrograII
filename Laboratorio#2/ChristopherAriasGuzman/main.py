import GestionVentas as gv
from Dominio import Factura

#Este metodo registrar facturas
def registrarfactura():
   gv.crearFactura(1,5000)
   
def imprimirfacturas():
    gv.imprimirfacturas()
    
def main():    
    while True:
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