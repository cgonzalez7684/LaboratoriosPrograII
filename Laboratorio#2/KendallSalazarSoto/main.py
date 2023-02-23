import GestionVentas as gv
from Dominio import Factura


# Este metodo registrar facturas
def registrarfactura():
    cliente = input("Ingrese el nombre del cliente: ")
    monto = float(input("Digitar el monto de la factura: "))
    categoriaVenta = input("Ingrese la categoría de la venta: ")
    impuestofactura = 0
    descuento = 0
    gv.crearFactura(cliente, monto, categoriaVenta, impuestofactura, descuento)


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
    print("Esto es fuera del while")


if __name__ == "__main__":
    main()
