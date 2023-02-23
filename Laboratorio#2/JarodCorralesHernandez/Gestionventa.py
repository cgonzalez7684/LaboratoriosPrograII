from Dominio import Factura
from datetime import datetime as dt

listadoFacturas = [] #list

formatoConseFact = "FACT#{0}" 
consecutivoFactura = 1


def encabezadoSistema():
    print("----------------------------------")   
    print("Opción #A : 5% de descuento")
    print("Opción #B : 10% de descuento")
    print("Opción #C : Por favor ingre el monto del descuento")
    print("----------------------------------")

def crearFactura(             
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
        
    
    except BaseException:
        print('Existe un error al crear la factura')
    
    
  
def imprimirfacturas():
    
    
    for n in listadoFacturas:
        print("---------------{0} {1}".format(n.idfactura, "factura en colones"))
        
        print("El monto de la factura es ",n.montofactura) 
        
        