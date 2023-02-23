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
                 nombreCliente,impuestofactura                 
                 ):
    
    try:
        ofactura = Factura() #instanciar una clase en un objeto (ya existe en memoria)   
        global consecutivoFactura
        numFact = str(consecutivoFactura).rjust(5,'0')
        ofactura.idfactura =  formatoConseFact.format(numFact) #"FACT#0001" #Quemar el dato / HardCode
        ofactura.fechafactura = dt.now()    
        ofactura.categoriaVenta = categoriaVenta
        ofactura.nombreCliente = nombreCliente
        ofactura.impuestofactura=  impuestofactura
        ofactura.montoIVA= montofactura + impuestofactura
        if (categoriaVenta == "A" or "a"):
            ofactura.montofactura = ofactura.montoIVA - (ofactura.montoIVA*0.05 ) 
             
        elif (categoriaVenta == "B" or "b"):
            ofactura.montofactura = ofactura.montoIVA - (ofactura.montoIVA*0.1 ) 
            
        elif (categoriaVenta == "C" or "c"):
            temp = int(input("Cual es el descuento deseado?"))
            ofactura.montofactura = ofactura.montoIVA - (ofactura.montoIVA * (temp / 100)) 
        
            
            
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
        print("Fecha de factura: ", n.fechafactura)
        print(f'Nombre del Cliente: ', n.nombreCliente)
        print("El monto de la factura es ",n.montofactura) 
        print("Categoria de descuento: ",n.categoriaVenta)
        print("I.V.A: ",n.impuestofactura)
       
        
        #El monto de la factura es 458789
        

