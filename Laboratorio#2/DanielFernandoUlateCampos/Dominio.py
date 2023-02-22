class Factura()
def _init_(self) -> None:
    self.idfactura = None
    self.fechafactura = None
    self.montofactura = None
    self.impuestofactura = None
    self.categoriaventa = None
    self.descuentoventa = None
    self.porcentajenew = None
    
def calcularImpuesto (self):
    self.impuestofactura = self.montofactura *0.13
    return self.impuestofactura

def calcularDescuento(self):
    if (self.categoriaventa =="a"):
        self.descuentoVenta = self.montofactura - (self.montofactura * 0.05)
    elif (self.categoriaventa == "b"):
        self.descuentoVenta = self.montofactura - (self.montofactura * 0.10)
    else:
        self.porcentajenew = float(input("Coloque el porcetaje de descuento por aplicar: "))
        self.descuentoVenta = self.montofactura - (self.montofactura * self.porcentajenew)
        
    return self.descuentoVenta