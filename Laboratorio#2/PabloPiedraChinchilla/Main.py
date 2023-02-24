import GestionVentas as gv
from Dominio import Factura



#Este metodo registrar facturas
def registrarfactura():
   monto = float(input("Digitar el monto de la factura: "))
  # if monto <=1000:
   #    monto *=0.05
   #elif monto <=2000:
    #   monto *=0.10
   #elif monto== nuevo_monto:
   tipoVenta=input("Ingrese porsentaje de descuento: Sea A,B,C\" \n")
   cliente_nombre=input("Nombre del cliente: ")
   gv.crearFactura( monto, tipoVenta, cliente_nombre)
   
   
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
    