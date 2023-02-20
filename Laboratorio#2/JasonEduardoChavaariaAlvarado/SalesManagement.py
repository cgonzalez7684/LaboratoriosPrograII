from Domain import Factura
from datetime import datetime as dt

listadoFacturas = [] #list

formatoConseFact = "FACT#{0}"  
consecutivoFactura = 1


def encabezadoSistema():
    print("----------------------------------")   
    print("Opción #1 : Crear facturas")
    print("Opción #2 : Imprimir facturas")
    print("----------------------------------")


def crearFacturas(             
                 montofactura,
                 categoriaVenta                 
                 ):
    
    try:
        ofactura = Factura()   
        global consecutivoFactura
        numFact = str(consecutivoFactura).rjust(5,'0')
        ofactura.idfactura =  formatoConseFact.format(numFact) 
        ofactura.fechafactura = dt.now    
        ofactura.montofactura = montofactura        
        ofactura.calculaImpuesto()    
        listadoFacturas.append(ofactura) 
        consecutivoFactura = consecutivoFactura + 1
      
    except ZeroDivisionError:
        print("Se esta dando una division entre cero")   
    except BaseException:
        print('Hay un error al crear la factura')
    
    
  
def imprimirfacturas():
    
    for n in listadoFacturas:
        print("---------------{0} {1}".format(n.idfactura, "factura en colones"))
      
        print("El monto de la factura es ",n.montofactura) 

        