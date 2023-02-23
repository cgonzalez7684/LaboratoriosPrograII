from Dominio import Factura
from datetime import datetime as dt

listadoFacturas = []
formatoConsecFactura = "FACT# {}"
consecutivoFactura = 1

def encabezadoSistema():
    print ("----------------------------------")
    print ("Opción #1 : Crear Factura")
    print ("Opción #2 : Imprimir Facturas")
    print ("==================================")

def menudescuentos():
    print ("\nCategoria #a : Aplica descuento de 5% ")
    print ("Categoria #b : Aplica descuento de 6%")
    print ("Categoria #c : Se ingresa manual el descuento que desea hacer")
    print ("==================================")

def crearFactura(montofactura, categoriaventa):

    ofactura = Factura()
    global consecutivoFactura
    numFactura = str(consecutivoFactura).rjust(5,'0')

    ofactura.idfactura = formatoConsecFactura.format(numFactura)
    ofactura.fechafactura = dt.now
    ofactura.montofactura = montofactura
    
    ofactura.categoriaventa = categoriaventa
    ofactura.calcularImpuesto()
    ofactura.calcularDescuento()

    listadoFacturas.append(ofactura)
    consecutivoFactura = consecutivoFactura + 1

def imprimirfacturas():

    for n in listadoFacturas :
        print ("=============Datos de factura=================")       
        print ("Id factura:  ", n.idfactura)
        print ("El monto de la factura es: ", n.montofactura)
        print ( "Categoria de venta: ",  n.categoriaventa)
        print ("Impuesto de ventas:  " , n.calcularImpuesto())
        print ("Monto a pagar con descuento: " , n.calcularDescuento())
        print ("-----------------------------------------")
        print ("Fecha de creación :  " , n.fechafactura())
