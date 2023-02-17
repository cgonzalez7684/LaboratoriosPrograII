import GestionVentas as gv
from Dominio import Factura

def descuentocategoria 
    monto_descuento = monto 
    if categoria == 'A'
    monto_descuento = monto_descuento - (monto_descuento * 0.05)
    elif  categoria  == 'B':
        monto_descuento  =  monto_descuento - (monto_descuento * 0.1)
    elif  categoria  == 'C':
        porcentaje  = float(input("Preguntar al administrador monto a rebajar"))
        descuento  =  porcentaje  /  100
        monto_descuento  =  monto_descuento - (monto_descuento * descuento)
    volver  monto_descuento


#Este metodo registrar facturas
def registrarfactura():
   monto = float(input("Digitar el monto de la factura: "))
   gv.crearFactura(monto)
   
def imprimirfacturas():
    gv.imprimirfacturas()

def categoriaVenta():
    categoria = float(input("Digitar categoria sobre descuento"))
    gv.categoriaVenta(categoria)
    

    
def main(): 
    

    while True:
        gv.encabezadoSistema()
        opcion = int(input("Digitar la opción sistema: "))
        if (opcion == 1):
            registrarfactura()
        elif (opcion == 2):  #y sino si
            imprimirfacturas()        
        else: #y sino
            continue
    print("Esto es fuera del while") 
        

if __name__ == "__main__":
    main()
    