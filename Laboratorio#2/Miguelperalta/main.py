import GestionVentas as gv
from Dominio import Factura
from GestionVentas import crearFactura, listadoFacturas, imprimirFacturas


# Este metodo registrar facturas
def registrarFactura(opcion):
   monto = float(input("Digitar el monto de la factura: "))
   categoriaVenta = str(input("Digite la categoria: "))
   factura = crearFactura(monto, categoriaVenta)
   if factura is not None:
      print("Factura registrada con éxito!")
      return factura    

def imprimir(factura):
    if factura is not None:
     factura.impresion()

def main(): 
    factura = None
    while True:
        print("----------------------------------")
        print("Opción #1 : Crear facturas")
        print("Opción #2 : Imprimir facturas")
        print("----------------------------------")
        
        opcion = int(input("Digitar la opción sistema: "))
        if (opcion == 1):
            factura = registrarFactura(opcion)
        
        elif (opcion == 2):
            imprimir(factura)

if __name__ == "__main__":
    main()