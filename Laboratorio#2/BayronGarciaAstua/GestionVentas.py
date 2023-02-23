from Dominio import Factura
import datetime

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
        fechaAhora = datetime.datetime.now()
        ofactura.idfactura =  formatoConseFact.format(numFact) #"FACT#0001" #Quemar el dato / HardCode
        ofactura.fechafactura = fechaAhora.strftime("%d/%m/%Y %H:%M:%S")
        ofactura.montofactura = montofactura    
        ofactura.categoriaVenta = categoriaVenta.upper()

        if ofactura.categoriaVenta == "A":
            ofactura.montofactura = ofactura.montofactura * 0.95

        elif ofactura.categoriaVenta == "B":
            ofactura.montofactura = ofactura.montofactura * 0.9
        
        elif ofactura.categoriaVenta == "C":
            montoDescuento = int(input("Digite el porcentaje del descuento: "))
            ofactura.montofactura = ofactura.montofactura * (1 - (montoDescuento/100))



        ofactura.calculaImpuesto()    
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
    except BaseException as e:
        print('Existe un error al crear la factura')
        print(e)
    
    
  
def imprimirfacturas():
    #iterar es saltar de elemento a elemento dentro de la colección
    
    for n in listadoFacturas:
        print("---------------{0} {1}".format(n.idfactura, "factura en colones"))
        #casting de dato convirtiendo de numero (int) a cadena de texto (str)
        print("El monto de la factura es ",n.montofactura) 
        #El monto de la factura es 458789
        print("La fecha de la factura es ",n.fechafactura) 
        print("El impuesto aplicado a la factura es %.2f" % round(n.impuestofactura, 2)) 
        #print("El nombre del cliente de la factura es ",n.nombreCliente) ------Comentado porque no se está seteando
        print("La Categoría de la venta de la factura es ",n.categoriaVenta)

