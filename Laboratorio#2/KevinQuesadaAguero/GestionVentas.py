from Dominio import Factura
from datetime import datetime as dt

listadoFacturas = [] #list

formatoConseFact = "FACT#{0}" 
consecutivoFactura = 1


def encabezadoSistema():
    print("----------------------------------")   
    print("Opción #1 : Crear facturas")
    print("Opción #2 : Imprimir facturas")
    print("----------------------------------")

def crearFactura(             
                 montofactura,
                 categoriaVenta                 
                 ):
    
   def crearFactura(montofactura, categoriaVenta):
    try:
        ofactura = Factura()  
        global consecutivoFactura
        numFact = str(consecutivoFactura).rjust(5,'0')
        ofactura.idfactura =  formatoConseFact.format(numFact) 
        ofactura.fechafactura = dt.now    
        ofactura.montofactura = montofactura        
        ofactura.calculaImpuesto()    
        
        if categoriaVenta == 'A':
            ofactura.descuentofactura = ofactura.montofactura * 0.05
            ofactura.montofactura -= ofactura.descuentofactura
        elif categoriaVenta == 'B':
            ofactura.descuentofactura = ofactura.montofactura * 0.1
            ofactura.montofactura -= ofactura.descuentofactura
        elif categoriaVenta == 'C':
            descuento = float(input("Ingrese el monto de descuento a aplicar: "))
            ofactura.descuentofactura = descuento
            ofactura.montofactura -= descuento
            
        listadoFacturas.append(ofactura) 
        consecutivoFactura = consecutivoFactura + 1
        
    except ZeroDivisionError:
        print("Se esta dando una division entre cero")   
    except BaseException:
        print('Existe un error al crear la factura')

    
  
def imprimirfacturas():
    for n in listadoFacturas:
        print("---------------{0} {1}".format(n.idfactura, "factura en colones"))
        print("Fecha factura: ", n.fechafactura())
        print("Nombre del cliente: ", n.nombreCliente)
        print("Monto de la factura: ", n.montofactura)
        print("Impuesto de la factura: ", n.impuestofactura)
        if hasattr(n, 'descuentofactura'):
            print("Descuento de la factura: ", n.descuentofactura)
        else:
            print("No hay descuento aplicado a la factura")
        print("-----------------------")

        

