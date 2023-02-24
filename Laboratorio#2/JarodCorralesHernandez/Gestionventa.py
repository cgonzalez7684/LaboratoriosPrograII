from Dominio import Factura
from datetime import datetime as dt

listadoFacturas = [] #list

formatoConseFact = "FACT#{0}" 
consecutivoFactura = 1


def encabezadoSistema():
    print("----------------------------------")   
    print("Opción #1 : Crear facturas ")
    print("Opción #B : Imprimir facturas")
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
        if (categoriaVenta == "A"):
            descuento = ofactura.montofactura * 0.05
            ofactura.montofactura = ofactura.montofactura - descuento
        elif(categoriaVenta == "B"): 
            descuento = ofactura.montofactura * 0.10
            ofactura.montofactura = ofactura.montofactura - descuento
        elif(categoriaVenta == "C"):
            descuento = int(input("Por favor indique el monto del descuento: "))
            ofactura.montofactura = ofactura.montofactura - descuento
    
    except BaseException:
        print('Existe un error al crear la factura')
    
    
  
def imprimirfacturas():
    
    
    for n in listadoFacturas:
        print("---------------{0} {1}".format(n.idfactura, "factura en colones"))
        
        print("El monto de la factura es ",n.montofactura) 
        
        