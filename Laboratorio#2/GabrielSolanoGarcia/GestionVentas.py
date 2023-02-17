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
    
    try:
        ofactura = Factura() #instanciar una clase en un objeto (ya existe en memoria)   
        global consecutivoFactura
        numFact = str(consecutivoFactura).rjust(5,'0')
        #montofactura = ofactura.calculaDescuento(montofactura, categoriaVenta)
        if categoriaVenta == "A":
            ofactura.idfactura =  formatoConseFact.format(numFact) #"FACT#0001" #Quemar el dato / HardCode
            ofactura.descuento = montofactura* 0.05
            ofactura.fechafactura = dt.now    
            ofactura.montofactura = montofactura - ofactura.descuento        
            ofactura.calculaImpuesto()    
            listadoFacturas.append(ofactura) #es el metodo que me permite agregar elementos a la lista
            consecutivoFactura = consecutivoFactura + 1
        elif categoriaVenta == "B":
            ofactura.idfactura =  formatoConseFact.format(numFact) #"FACT#0001" #Quemar el dato / HardCode
            ofactura.descuento = montofactura* 0.1
            ofactura.fechafactura = dt.now    
            ofactura.montofactura = montofactura - ofactura.descuento      
            ofactura.calculaImpuesto()    
            listadoFacturas.append(ofactura) #es el metodo que me permite agregar elementos a la lista
            consecutivoFactura = consecutivoFactura + 1
        elif categoriaVenta == "C":
            print("si entro al if")
            ofactura.idfactura =  formatoConseFact.format(numFact) #"FACT#0001" #Quemar el dato / HardCode
            descuentoAplicar = int(input("Digite el descuento que se le va a hacer a la factura: "))
            ofactura.descuento = montofactura * descuentoAplicar / 100
            print("si leyo el descuento")
            ofactura.fechafactura = dt.now    
            ofactura.montofactura = montofactura - ofactura.descuento
            print("si aplico el descuento")
            ofactura.calculaImpuesto()    
            listadoFacturas.append(ofactura) #es el metodo que me permite agregar elementos a la lista
            consecutivoFactura = consecutivoFactura + 1
        else:
            print("Debe de digitar una opcion entre A/B/C")
        
        #n = 2
        #x = 0
        #resultado = n / x
    #consecutivoFactura += 1 
    except ZeroDivisionError:
        #Mandar registrar el error en bitacoras (Tabla BD / Archivo Txt)
        #Informarle al usuario de error con un mensaje mas amigable
        print("Se esta dando una division entre cero")   
    except BaseException:
        print('Existe un error al crear la factura')
    
    
  
def imprimirfacturas():
    #iterar es saltar de elemento a elemento dentro de la colección
    
    for n in listadoFacturas:
        print("---------------{0} {1}".format(n.idfactura, "factura en colones"))
        #casting de dato convirtiendo de numero (int) a cadena de texto (str)
        print("El montofactura de la factura es ",n.montofactura) 
        print("El descuento de la factura es de ", n.descuento)   

