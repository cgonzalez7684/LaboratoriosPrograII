import GestionVentas as gv
from Dominio import Factura


#Este metodo registrar facturas
def registrarfactura():
   nombre = input("digite su nombre: ")
   monto= float(input("Digitar el monto de la factura: "))
   montopr=monto
   catventas= input("introduzca la categoria de la venta: ")
   if (catventas == "A" or catventas == "a"):
    montoR = monto - (monto * 0.05)
   elif(catventas == "B" or catventas == "b"):
      montoR = monto - (monto * 0.10)
   elif(catventas == "C" or catventas == "c"):
    MontoA = float(input("Digitar el descuento de la factura: "))
    MontoA = MontoA / 100
    montoR = monto - (monto * MontoA)

   gv.crearFactura(montoR,catventas,nombre, montopr)
   
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
    