import gestion_ventas as gv
from Dominio import Factura


# Este metodo registrar facturas
def registrarfactura():
    desc = 0
    monto = float(input("Digitar el monto de la factura: "))
    cat = str(input("Digite la categoria (A,B,C): "))
    if cat == 'C':
        desc = float(input("Digite el descuento de la factura: "))
    customer_name = input("Digite el nombre del cliente: ")

    gv.crearFactura(monto, cat, desc, customer_name)


def imprimirfacturas():
    gv.imprimirfacturas()


def main():

    while True:
        gv.encabezadoSistema()
        opcion = int(input("Digitar la opción sistema: "))
        if (opcion == 1):
            registrarfactura()
        elif (opcion == 2):  # y sino si
            imprimirfacturas()
        else:  # y sino
            continue


if __name__ == "__main__":
    main()
