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
  
    

def crearFactura( montofactura):
    
    try:
        ofactura = Factura() #instanciar una clase en un objeto (ya existe en memoria)   
        global consecutivoFactura
        numFact = str(consecutivoFactura).rjust(5,'0')
        
        ofactura.nombreCliente = input("Ingresa el nombre del cliente: ")
        ofactura.idfactura =  formatoConseFact.format(numFact) #"FACT#0001" #Quemar el dato / HardCode
        ofactura.fechafactura = dt.now()   
        ofactura.montofactura = montofactura        
        ofactura.calculaImpuesto()
        
        categoriaVenta = input("Ingrese la categoria de venta (A, B o C): ")
        ofactura.categoriaVenta = categoriaVenta
        
        ofactura.calcularDescuento()
        ofactura.impuestofactura
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
        print("------------------------------------------------------------------")
        print("----------------{0} {1}".format(n.idfactura, " "))
        print("FACTURAR A")
        print("Cliente: ", n.nombreCliente)
        #casting de dato convirtiendo de numero (int) a cadena de texto (str)
        print("Fecha de la factura: ", n.fechafactura.strftime('%Y-%m-%d %H:%M:%S'))
        print("Monto ",n.montofactura, "Colones" )
        #El monto de la factura es 458789
        print("Tipo de Categoria Venta: ", n.categoriaVenta)
        print("Descuento: {0:.2f}".format(n.descuento)) 
        sub = n.montofactura - n.descuento
        total = (sub * 0.13) + sub 
        impuesto = sub * 0.13
        print("Subtotal: ", sub)
        print("Total: ", total)
        print("IVA aplicado: ", impuesto)
        print("------------------------------------------------------------------")
            

