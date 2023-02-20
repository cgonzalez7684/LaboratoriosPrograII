class Factura:
    def __init__(self) -> None:
        self.idfactura = None
        self.fechafactura = None        
        self.montofactura = None
        self.impuestofactura = None 
        self.nombreCliente = None
        self.categoriaVenta = None
    
    def calculaImpuesto(self):
        self.impuestofactura = self.montofactura * 0.13
        return self.impuestofactura

    def calcularDescuento(self):
        if isinstance(self.categoriaVenta, str):
            categoria = self.categoriaVenta.upper()
            if categoria == 'A':
                self.descuento = self.montofactura * 0.05
            elif categoria == 'B':
                self.descuento = self.montofactura * 0.1
            elif categoria == 'C':
                montoDescuento = float(input("Ingrese el monto de descuento a rebajar: "))
                self.descuento = montoDescuento
            else:
                print("Categoria de venta no valida")
        else:
            print("Tipo de categoria no valido")
            
listadoFacturas = []