from curses import nocbreak
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
                 nombre               
                 ):
    
    try:
        ofactura = Factura() #instanciar una clase en un objeto (ya existe en memoria)   
        global consecutivoFactura
        numFact = str(consecutivoFactura).rjust(5,'0')
        ofactura.idfactura =  formatoConseFact.format(numFact) #"FACT#0001" #Quemar el dato / HardCode
        ofactura.fechafactura = dt.now()   
        ofactura.montofactura = montofactura 
        ofactura.nombreCliente = nombre 
        ofactura.calculaImpuesto()    
        listadoFacturas.append(ofactura) #es el metodo que me permite agregar elementos a la lista
        consecutivoFactura = consecutivoFactura + 1
        
        if (categoriaVenta== "A"):
            descuento= ofactura.montofactura *0.05
            ofactura.montofactura = ofactura.montofactura - descuento
        elif (categoriaVenta == "B"):
            descuento = ofactura.montofactura *0.1
            ofactura.montofactura = ofactura.montofactura - descuento
        elif (categoriaVenta =="C"):
             descuento = input("Ingrese el monto seleccionado para el descuento")
             ofactura.montofactura = ofactura.montofactura - descuento
        else:     
            print("Categoría de venta inválida")

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
        print("El monto de la factura es:",n.montofactura) 
        #El monto de la factura es 458789
        print("La fecha y la hora de la factura:",n.fechafactura)
         #La fecha y la hora de la es 21/07/23
        print("El monto del impuesto es:",n.impuestofactura)
        #El monto del impuesto es:
        print("El Nombre de la factura es:",n.nombreCliente)
        #El Nombre de la factura es:  
        print("La categoria venta es:",n.categoriaVenta)
         #La categoria venta es :