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
                 nombreCliente                    
                 ):
    
    try:
        ofactura = Factura() 
        global consecutivoFactura
        numFact = str(consecutivoFactura).rjust(5,'0')
        if categoriaVenta == "A" :
            ofactura.nombre = nombreCliente
            ofactura.idfactura =  formatoConseFact.format(numFact) 
            ofactura.descuento = montofactura* 0.05
            ofactura.fechafactura = dt.now()    
            ofactura.montofactura = montofactura - ofactura.descuento        
            ofactura.calculaImpuesto()    
            listadoFacturas.append(ofactura) 
            consecutivoFactura = consecutivoFactura + 1
        elif categoriaVenta == "B":
            ofactura.nombre = nombreCliente
            ofactura.idfactura =  formatoConseFact.format(numFact) 
            ofactura.fechafactura = dt.now() 
            ofactura.descuento = montofactura* 0.1
            ofactura.montofactura = montofactura - ofactura.descuento        
            ofactura.calculaImpuesto()    
            listadoFacturas.append(ofactura) 
            consecutivoFactura = consecutivoFactura + 1
        elif categoriaVenta == "C":
            ofactura.nombre = nombreCliente
            ofactura.idfactura =  formatoConseFact.format(numFact) 
            ofactura.fechafactura = dt.now 
            descuentoC =  int(input("Digite el porcentaje a descontar al cliente:"))  
            ofactura.descuento= montofactura * descuentoC /100    
            ofactura.fechafactura = dt.now()    
            ofactura.montofactura = montofactura - ofactura.descuento 
            ofactura.calculaImpuesto()    
            listadoFacturas.append(ofactura) 
            consecutivoFactura = consecutivoFactura + 1  
        else:
            print("No digito ninguna opcion posible")
            exit
            
            
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
        print("El monto de la factura es: ",n.montofactura) 
        print("La fecha de la factura es: ",n.fechafactura)
        print("El nombre del cliente es: ",n.nombre)
        print("El descuento de la venta es de:  ",n.descuento)
        

