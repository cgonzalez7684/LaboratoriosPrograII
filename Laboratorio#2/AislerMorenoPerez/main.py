import GestionVentas as gv
from Dominio import Factura

#Este metodo registrar facturas
def registrarfactura():
   Nombre = input("Digita el nombre del cliente: ")
   monto = float(input("Digitar el monto de la factura: "))
   montoReal = 0
   if (monto >= 10000):
    montoReal = monto - (monto * 0.5)
    gv.crearFactura(montoReal,"A",Nombre)

   elif(monto>=15000):
    
    montoReal = monto - (monto * 0.10)
    gv.crearFactura(montoReal,"B",Nombre)

   elif(monto>=20000):
    MontoAdmin = float(input("Digitar el descuento de la factura: "))
    montoReal = monto - (monto * MontoAdmin)
    gv.crearFactura(montoReal,"C",Nombre)

    
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