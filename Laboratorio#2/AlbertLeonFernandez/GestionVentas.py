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
        ofactura = Factura() #instanciar una clase en un objeto (ya existe en memoria)   
        global consecutivoFactura
        numFact = str(consecutivoFactura).rjust(5,'0')
        ofactura.idfactura =  formatoConseFact.format(numFact) #"FACT#0001" #Quemar el dato / HardCode
        ofactura.fechafactura = dt.now    
        ofactura.categoriaVenta = categoriaVenta
        ofactura.nombreCliente = nombreCliente
        
        CATEGORIA_A = "A"
        CATEGORIA_B = "B"
        CATEGORIA_C = "C"

        # categoriaVenta = input("Ingrese la categoría de la venta (A, B o C): ")
        # montofactura = input("Ingrese el monto de la factura: ")  
        if categoriaVenta == CATEGORIA_A:
            montofactura = montofactura-(montofactura*0.05) # descuento del 5%
        elif categoriaVenta == CATEGORIA_B:
            montofactura = montofactura-(montofactura*0.01) # descuento del 10%
        elif categoriaVenta == CATEGORIA_C:
            monto_descuento = float(input("Ingrese el monto de descuento a rebajar de la factura en decimales: "))
            montofactura = montofactura - (montofactura*monto_descuento)  # descuento personalizado
        else:
            print("La categoría ingresada no es válida. Por favor, ingrese A, B o C.")

        print("El monto a facturar es: ", montofactura)
    
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
        print("****************************************************************")
        print("---------------{0} {1}".format(n.idfactura, "factura en colones"))
        #casting de dato convirtiendo de numero (int) a cadena de texto (str)
        print(f'Cliente {n.nombreCliente}, categoria de descuento {n.categoriaVenta}')
        print(f'El monto de la factura es ${n.montofactura} colones')
        print("****************************************************************")
        #No se cual es el error me retorna un None en el montofactura cuando realizo la impresion de factura
        

