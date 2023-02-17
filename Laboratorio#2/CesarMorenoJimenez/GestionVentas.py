from Dominio import Factura
from datetime import datetime as dt

listadoFacturas = [] #list

def crearFactura(idfactura,                 
                 montofactura                 
                 ):
    
    ofactura = Factura() #instanciar una clase en un objeto (ya existe en memoria)
    ofactura.idfactura = "FACT#0001" 
    ofactura.fechafactura = dt.now    
    ofactura.montofactura = 458789
    ofactura.calculaImpuesto()    
    listadoFacturas.append(ofactura) #es el metodo que me permite agregar elementos a la lista
  
def imprimirfacturas():
    #iterar es saltar de elemento a elemento dentro de la colección
    for n in listadoFacturas:
        print("---------------{0} {1}".format(n.idfactura, "factura en colones"))
        #casting de dato convirtiendo de numero (int) a cadena de texto (str)
        print("El monto de la factura es ",n.montofactura) 
        #El monto de la factura es 458789
        

