import GestionVentas as gv
from Dominio import Factura


#Este metodo registrar facturas
def registrarfactura():
   monto = float(input("Digitar el monto de la factura:\n"))
   
   #Solicitud del tipo de categoria de factura al usuario
   categoria = int(input("\nDigite el la categoria de la factura: \n1-A\n2-B\n3-C\n\n"))
   while categoria <= 0 or categoria > 3:
       print ("Intente de nuevo, la categoria seleccionada no es valida")
       categoria = int(input("Digite la categoria de la factura: \n1-A\n2-B\n3-C\n\n"))
   
   nombre = str(input("Digite el nombre de la persona a quien ira dirigida la factura: \n"))
   
   gv.crearFactura(monto, categoria, nombre)
   
def imprimirfacturas():
    gv.imprimirfacturas()
    

def main(): 
       
    while True:
        gv.encabezadoSistema()
        opcion = int(input("Digitar la opción sistema: \n"))
        if (opcion == 1):
            registrarfactura()
        elif (opcion == 2):  #y sino si
            imprimirfacturas()        
        else: #y sino
            continue
    print("Esto es fuera del while") 
        

if __name__ == "__main__":
    main()
    