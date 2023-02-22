import GestionVentas as gv
from Dominio import Factura

def registrarfactura():
    
    monto = float(input("Digite el monto a facturar : "))
    gv.menudescuento()
    categoria = input("Coloque la categoria de la venta: ")
    
    gv.crearFactura(monto, categoria)
    
def imprimifacturas():
    gv.imprimirfacturas()
    
def main():
    
    while True:
        gv.encabezadosSistema()
        opcion = int(input("Digite una opción del Sistema"))
        if(opcion ==1):
            registrarfactura()
        elif(opcion ==2):
            imprimifacturas()
        else:
            continue
        
if __name__=="__main__":
    main()