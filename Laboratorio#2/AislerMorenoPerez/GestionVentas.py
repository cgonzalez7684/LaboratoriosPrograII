from Dominio import Factura
from datetime import datetime as dt 

listadoFacturas = [] #list

formatoConseFact = "FACT#{0}" 
consecutivoFactura = 1


def encabezadoSistema():
    print("----------------------------------")   
    print("Opción #1 : Crear facturas")
    print("Opción #2 : Imprimir facturas")
    print("Opción #3 : Salir")
    print("----------------------------------")
    

def crearFactura(             
                 montofactura,
                 categoriaVenta,
                 nombreCliente                 
                 ):
    
    
        ofactura = Factura() #instanciar una clase en un objeto (ya existe en memoria)   
        global consecutivoFactura
        numFact = str(consecutivoFactura).rjust(5,'0')
        ofactura.idfactura =  formatoConseFact.format(numFact) #"FACT#0001" #Quemar el dato / HardCode
        ofactura.fechafactura = dt.now   
        ofactura.montofactura = montofactura        
        ofactura.calculaImpuesto()
        ofactura.nombreCliente = nombreCliente
        ofactura.categoriaVenta = categoriaVenta   
        listadoFacturas.append(ofactura) #es el metodo que me permite agregar elementos a la lista
        consecutivoFactura = consecutivoFactura + 1
        #n = 2
        #x = 0
        #resultado = n / x
    #consecutivoFactura += 1 
       
    
    
    
  
def imprimirfacturas():
    #iterar es saltar de elemento a elemento dentro de la colección
    try:
        for n in listadoFacturas:
            print("El nombre del cliente es: " + n.nombreCliente)
            print("Fecha de la factura: " + n.fechafactura)
            print("La compra es Categoria: " + n.categoriaVenta )
            print("---------------{0} {1}".format(n.idfactura, "factura en colones"))
        
            print("El monto de la factura es ",n.montofactura) 
        
    except BaseException:
        print('Existe un error al imprimir la factura')

        
    