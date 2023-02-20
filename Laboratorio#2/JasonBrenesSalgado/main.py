import GestionVentas as gv
from Dominio import Factura

def registrarfactura():
    nombrecliente = input("Ingrese nombre del cliente : ")
    monto = float(input("Digite el monto de la factura :  "))
    categoria = input("Ingrese la categoria de la venta: ")

    gv.crearFactura(monto, categoria, nombrecliente)

def imprimifacturas():
    gv.imprimirfacturas()
1

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


if __name__=="__main__":
    main()



