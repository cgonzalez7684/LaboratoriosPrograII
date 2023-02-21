def registrarfactura():
    
    monto = float(input("Digite el monto de la factura :  "))
    gv.menudescuentos()
    categoria = input("Ingrese la categoria de la venta: ")

    gv.crearFactura(monto, categoria)

def imprimifacturas():
    gv.imprimirfacturas()


def main():

    while True:
        gv.encabezadoSistema()
        opcion = int(input("Digite una opción del sistema: "))
        if(opcion ==1):
            registrarfactura()
        elif (opcion ==2):
            imprimifacturas()
        else:
            continue


if _name=="__main_":
    main()