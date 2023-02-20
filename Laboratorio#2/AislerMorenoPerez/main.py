import GestionVentas as gv
from Dominio import Factura

#Este metodo registrar facturas
def registrarfactura():

   Nombre = input("Digita el nombre del cliente: ")
   categoriaVenta = input("Digita la catergoria de la venta: ")
   monto = float(input("Digitar el monto de la factura: "))
   montoReal = 0

   if (categoriaVenta == "A" or categoriaVenta == "a"):
    montoReal = monto - (monto * 0.05)
    gv.crearFactura(montoReal,categoriaVenta,Nombre)

   elif(categoriaVenta == "B" or categoriaVenta == "b"):
    
    montoReal = monto - (monto * 0.10)
    gv.crearFactura(montoReal,categoriaVenta,Nombre)

   elif(categoriaVenta == "C" or categoriaVenta == "c"):
    MontoAdmin = float(input("Digitar el descuento de la factura: "))
    MontoAdmin = MontoAdmin / 100
    montoReal = monto - (monto * MontoAdmin)
    gv.crearFactura(montoReal,categoriaVenta,Nombre)
   

def imprimirfacturas():
    gv.imprimirfacturas()  

def logica():
    
    
    while(True):
        gv.encabezadoSistema()
        opcion = int(input("Digitar la opción sistema: "))

        if (opcion == 1):
            registrarfactura()
            
        elif (opcion == 2):  #y sino si
            print()
            imprimirfacturas()
            
        elif(opcion == 3):
            break

        else: #y sino
            continue

    
def main(): 
       
    logica()
        

if __name__ == "__main__":
    main()