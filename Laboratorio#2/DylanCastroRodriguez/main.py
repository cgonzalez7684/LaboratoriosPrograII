import GestionVentas as gv
from Dominio import Factura

#Este metodo registrar facturas
def registrarfactura():
   monto = float(input("Cual es el monto de la factura?: "))
   cdescuento = input("Cual es la categoria del descuento a efectuar (A, B, C): ")
   gv.crearFactura(monto, cdescuento)
   
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