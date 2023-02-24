
class Factura:
    def __init__(self) -> None:
        self.idfactura = None
        self.fechafactura = None        
        self.montofactura = None
        self.impuestofactura = None 
        self.nombreCliente = None
        self.categoriaVenta = None
        self.descuentoVenta = None
        self.categoriaC = None
    
    def calculaImpuesto(self):
        self.impuestofactura = self.montofactura * 0.13
        return self.impuestofactura
    
    def calculaDescuento(self):
        if(self.categoriaVenta == "A"):
            self.descuentoVenta = self.montofactura - (self.montofactura * (5 / 100))
        elif(self.categoriaVenta == "B"):
            self.descuentoVenta = self.montofactura - (self.montofactura * (10 / 100))
        elif(self.categoriaVenta == "C"):
            self.categoriaC = float(input("Digitar el porcentaje de descuento que desea aplicar: "))
            self.descuentoVenta = self.montofactura - (self.montofactura * (self.categoriaC / 100))
        return self.descuentoVenta
    
listadoFacturas = []