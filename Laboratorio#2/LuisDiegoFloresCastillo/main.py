# Main
import GestionVentas as gv
from Dominio import Factura


def registrarfactura():
    # Inicializar el monto como un float
    monto = float(input("Digitar el monto de la factura: "))

    # Inicializar el nombre del cliente
    nombre_cliente = input("Digite el nombre del cliente: ")

    # Inicializar la fecha
    fecha = input("Digite la fecha de la factura")

    # Verificar la categoría de venta
    categoriaVenta = input("Digite la categoría de la venta: ")

    # Aplicar el descuento correspondiente
    if categoriaVenta == 'A':
        monto = monto * 0.95
    elif categoriaVenta == 'B':
        monto = monto * 0.9
    elif categoriaVenta == 'C':
        descuento = float(input("Digite el valor del descuento: "))
        monto = monto - descuento

    # Crear la factura con los atributos establecidos anteriormente
    gv.crearFactura(monto, nombre_cliente, fecha, "A",)
    gv.crearFactura(monto, "A", "B", "C")


def imprimirfacturas():
    gv.imprimirfacturas()


def main():

    while True:
        gv.encabezadoSistema()
        opcion = int(input("Digitar la opción sistema: "))
        if (opcion == 1):
            registrarfactura()
        elif (opcion == 2):

            for factura in imprimirfacturas():
                print("ID Factura: ", factura.id_factura)
                print("Fecha Factura: ", factura.fecha)
                print("Monto Factura: ", factura.monto)
                print("Nombre Cliente: ", factura.nombre_cliente)
                print("Categoria Venta: ", factura.categoria_venta)
        else:
            break


if __name__ == "__main__":
    main()
