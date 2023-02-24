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
    
    if categoriaVenta == 'A':
            ofactura.descuentofactura = ofactura.montofactura * 0.05
            ofactura.montofactura -= ofactura.descuentofactura
        elif categoriaVenta == 'B':
            ofactura.descuentofactura = ofactura.montofact
listadoFacturas = []