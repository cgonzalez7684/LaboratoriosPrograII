from Dominio import Factura
from datetime import datetime as dt

listadoFacturas = []
formatoConsecFactura = "FACT# {}"
consecutivoFactura = 1

def encabezadoSistema():
    print ("--------------------------------------")
    print ("Primera Opción : Crear Factura")
    print ("Segunda Opción : Imprimir Facturas")
    print ("--------------------------------------")
    
def menudescuentos():
    print ("\nCategoria A : Tiene un descuento del 5% ")
    print ("Categoria B : Tiene un descuento del 6%")
    print ("Categoria C : El descuento por aplicar, se debe ingresar manualmente")
    print ("------------------------------------")
    
def crearFactura(montofactura, categoriaventa):
    
    ofactura = Factura()
    global consecutivoFactura
    numFactura = str(consecutivoFactura).rjust(5,"0")
    
    ofactura.idfactura = formatoConsecFactura.format(numFactura)
    ofactura.fechafactura = dt.now
    ofactura.montofactura = montofactura
    
    ofactura.categoriaventa = categoriaventa
    ofactura.calcularImpuesto()
    ofactura.calcularDescuento()
    
    listadoFacturas.append(ofactura)
    consecutivoFactura = consecutivoFactura + 1
    
def imprimirfacturas():
    
    for n in listadoFacturas:
        print("===========Detalles de la Factura===========")
        print("ID de factura: ", n.idfactura)
        print("El monto facturado es:" , n.montofactura)
        print("Categoria de la Venta:" , n.categoriaventa)
        print("Impuesto de la Venta:" , n.calcularImpuesto())
        print("Monto final a pagar: " , n.calcularDescuento())
        print("--------------------------------------------")
        print("Fecha de creación : " , n.fechafactura())
        
        
        
        
        
        