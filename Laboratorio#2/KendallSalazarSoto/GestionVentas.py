from Dominio import Factura
from datetime import datetime

listadoFacturas = []  # list

formatoConseFact = "FACT#{0}"
consecutivoFactura = 1


def encabezadoSistema():
    print("----------------------------------")
    print("Opción #1 : Crear facturas")
    print("Opción #2 : Imprimir facturas")
    print("----------------------------------")


def crearFactura(
    cliente,
    montofactura,
    categoriaVenta,
    impuestofactura,
    descuento
):

    try:
        ofactura = Factura()  # instanciar una clase en un objeto (ya existe en memoria)
        global consecutivoFactura
        numFact = str(consecutivoFactura).rjust(5, '0')
        ofactura.idfactura = formatoConseFact.format(
            numFact)  # "FACT#0001" #Quemar el dato / HardCode
        ofactura.nombreCliente = cliente
        ofactura.fechafactura = datetime.now()
        ofactura.montofactura = montofactura
        ofactura.categoriaVenta = categoriaVenta
        ofactura.impuestofactura = impuestofactura
        ofactura.descuento = descuento
        if (categoriaVenta == 'A'):
            ofactura.descuento = 0.05
        elif (categoriaVenta == 'B'):
            ofactura.descuento = 0.10
        elif (categoriaVenta == 'C'):
            descuento = float(input("Digite el descuento a aplicar: "))
            ofactura.descuento = descuento / 100
        ofactura.calculaImpuesto()
        # es el metodo que me permite agregar elementos a la lista
        listadoFacturas.append(ofactura)
        consecutivoFactura = consecutivoFactura + 1
        # n = 2
        # x = 0
        # resultado = n / x
    # consecutivoFactura += 1
    except ZeroDivisionError:
        # Mandar registrar el error en bitacoras (Tabla BD / Archivo Txt)
        # Informarle al usuario de error con un mensaje mas amigable
        print("Se esta dando una division entre cero")
    except BaseException:
        print('Existe un error al crear la factura')


def imprimirfacturas():
    # iterar es saltar de elemento a elemento dentro de la colección

    for n in listadoFacturas:
        print(
            "---------------{0} {1}".format(n.idfactura, "factura en colones"))
        # casting de dato convirtiendo de numero (int) a cadena de texto (str)
        print(f"El monto de la factura es: {n.montofactura}")
        # El monto de la factura es 458789
        print(f"Nombre del cliente: {n.nombreCliente}")
        print(f"Fecha: {n.fechafactura}")
        print(f"Categoría: {n.categoriaVenta}")
        print(f"Impuesto: {n.impuestofactura}")
        print(f"Descuento: {n.descuento}")
        print(
            f"Monto Total: {(n.montofactura * 0.13 + n.montofactura) - ((n.montofactura * 0.13 + n.montofactura) * n.descuento)}")
