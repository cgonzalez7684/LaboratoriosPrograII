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
    
def calcular_descuento(monto,categoria):
    montodescuento = monto
    if categoria == "A" or "a":
        montodescuento = montodescuento - (montodescuento * 0.05)
    elif categoria == "B" or "b":
        montodescuento = montodescuento - (montodescuento * 0.1)
        pass
    elif categoria == "C" or "c":
        porcentaje = float(input("Digite el porcentaje para aplicar como descuento: "))
        descuento = porcentaje / 100
        montodescuento = montodescuento - (montodescuento * descuento)
    return montodescuento

def crearFactura(             
                 montofactura,
                 categoriaVenta,
                 nombrecliente                 
                 ):
    
    try:
        ofactura = Factura() #instanciar una clase en un objeto (ya existe en memoria)   
        global consecutivoFactura
        numFact = str(consecutivoFactura).rjust(5,'0')
        ofactura.idfactura =  formatoConseFact.format(numFact) #"FACT#0001" #Quemar el dato / HardCode
        ofactura.fechafactura = dt.now    
        ofactura.montofactura = montofactura
        ofactura.categoriaVenta = categoriaVenta
        ofactura.nombreCliente = nombrecliente
        ofactura.calculaImpuesto()    
        listadoFacturas.append(ofactura) #es el metodo que me permite agregar elementos a la lista
        consecutivoFactura = consecutivoFactura + 1
        ofactura.montofinal = calcular_descuento(montofactura,categoriaVenta)
        
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
        print("El monto original de la factura es de ",n.montofactura) 
        print("El monto a pagar de impuestos ",n.impuestofactura)
        print("El nombre del cliente a facturar es: ",n.nombreCliente)
        print("La categoria de venta es: ",n.categoriaVenta)
        print("El monto con descuento es: ",n.montofinal)
        