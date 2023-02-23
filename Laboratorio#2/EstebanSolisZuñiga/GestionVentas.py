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

def tiposDescuentos():
    print("----------------------------------")   
    print("Categoría #A : Descuento de 5%")
    print("Categoría #B : Descuento de 10%")
    print("Categoría #C : Descuento manual del usuario")
    print("----------------------------------")

def crearFactura(             
                 montofactura,
                 categoriaVenta, nombreCliente                 
                 ):
    
    try:
        ofactura = Factura() #instanciar una clase en un objeto (ya existe en memoria)   
        global consecutivoFactura
        numFact = str(consecutivoFactura).rjust(5,'0')
        ofactura.idfactura =  formatoConseFact.format(numFact) #"FACT#0001" #Quemar el dato / HardCode
        ofactura.fechafactura = dt.now    
        ofactura.montofactura = montofactura
        ofactura.categoriaVenta = categoriaVenta
        ofactura.nombreCliente = nombreCliente     
        ofactura.calculaImpuesto()
        ofactura.calculaDescuento()    
        listadoFacturas.append(ofactura) #es el metodo que me permite agregar elementos a la lista
        consecutivoFactura = consecutivoFactura + 1
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
        print("El nombre del cliente es: ",n.nombreCliente)
        print("El monto de la factura es ",n.montofactura) 
        #El monto de la factura es 458789
        print ("La categoria de venta es: ",  n.categoriaVenta)
        print ("El impuesto de ventas es:  " , n.calculaImpuesto())
        print ("El monto a pagar con descuento es: " , n.calculaDescuento())
        print ("La eecha de creación de la factura es:  " , n.fechafactura())
        print ("-----------------------------------------")
        
        

