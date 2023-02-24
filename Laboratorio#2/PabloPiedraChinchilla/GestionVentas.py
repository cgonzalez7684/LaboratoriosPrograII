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
                 categoriaVenta, nombreCliente                 
                 ):
    
    try:
        ofactura = Factura() #instanciar una clase en un objeto (ya existe en memoria)   
        global consecutivoFactura
        numFact = str(consecutivoFactura).rjust(5,'0')
        ofactura.idfactura =  formatoConseFact.format(numFact) #"FACT#0001" #Quemar el dato / HardCode
        ofactura.fechafactura = dt.now
        ofactura.categoriaVenta = categoriaVenta    
        ofactura.montofactura = montofactura  
        ofactura.nombreCliente = nombreCliente     
        ofactura.calculaImpuesto()  
        
        Venta_A = "A" or "a"
        Venta_B = "B" or "b"
        Venta_C = "C" or "c"
        
        if categoriaVenta == Venta_A:
            (montofactura) = montofactura-(montofactura*0.05) # menos el 5%
        elif (categoriaVenta) == Venta_B:
            montofactura = montofactura-(montofactura*0.10) # menos el 10%
        elif (categoriaVenta) == Venta_C:
            descuento_C = float(input("Ingrese nuevo descuento autorizado: "))
            montofactura = montofactura - (montofactura*descuento_C)  # descuento por el admin
        else:
            print("La categoría ingresada no es correcta, favor intente nuevamente...!!!")

        print("El monto a facturar es: ", montofactura)
        
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
        print("El monto de la factura es ",n.montofactura) 
        #El monto de la factura es 458789
        print("El nombre del cliente es: ",n.nombreCliente)
        
