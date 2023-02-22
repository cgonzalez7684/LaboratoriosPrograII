import GestionVentas as gv
from Dominio import Factura


#Este metodo registrar facturas
def registrarfactura():
   monto = float(input("Digitar el monto de la factura: "))
   nombre= str(input("Digite el nombre de la persona a realizar la factura: "))
   descuento = str(input("Digite el descuento a conveniencia las opciones son A=5%, B=10%, C=Descuento a su parecer"))
   gv.crearFactura(monto, descuento, nombre)

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
