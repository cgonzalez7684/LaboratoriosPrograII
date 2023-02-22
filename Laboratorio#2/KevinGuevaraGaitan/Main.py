import GestionVentas as gv
from Dominio import Factura


#Este metodo registrar facturas
def registrarfactura():
    
    monto = float(input("Digitar el monto de la factura: "))
    gv.crearFactura(monto)
    
    monto = float(input("Digite el monto de la factura :  "))
    gv.menudescuentos()
    categoria = input("Ingrese la categoria de la venta: ")

    gv.crearFactura(monto, categoria)

def imprimifacturas():
    gv.imprimirfacturas()

def main():

    while True:
        gv.encabezadoSistema()
        opcion = int(input("Digite una opción del sistema: "))
        if(opcion ==1):
            registrarfactura()
        elif (opcion ==2):
            imprimifacturas()
        else:
            continue
    print("Esto es fuera del while") 
        

if __name__ == "__main__":
    main()
