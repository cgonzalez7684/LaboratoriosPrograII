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
                 categoriaVenta,
                 nombreCliente,                  
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
        if (categoriaVenta=="A" or "a"):
            descuento = ofactura.montofactura * 5 /100
            ofactura.montofactura = ofactura.montofactura - descuento
        elif (categoriaVenta=="B" or "b"):
            descuento = ofactura.montofactura * 10 /100
            ofactura.montofactura = ofactura.montofactura - descuento
        elif (categoriaVenta=="C" or "c"):
            descuento = input("Ingrese el monto seleccionado para el descuento: ")
            ofactura.montofactura = ofactura.montofactura - (ofactura.montofactura  * ((descuento) /100))
        #n = 2
        #x = 0
        #resultado = n / x
    #consecutivoFactura += 1 
        listadoFacturas.append(ofactura) #es el metodo que me permite agregar elementos a la lista
        consecutivoFactura = consecutivoFactura + 1

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
        print("El monto de la factura es ",n.montofactura) 
        #El monto de la factura es 458789
        print("Nombre del cliente: ", n.nombreCliente)
        print("Categoria de descuento: ",n.categoriaVenta)
        print("Fecha de factura: ", n.fechafactura)