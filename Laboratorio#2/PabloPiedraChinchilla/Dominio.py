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
        if (self.categoriaventa =="a"):
            self.descuentoVenta = self.montofactura  - (self.montofactura * 0.05) 
        elif(self.categoriaventa =="b"):
            self.descuentoVenta = self.montofactura - (self.montofactura * 0.10)
        else:
            self.porcentajenew = float(input("Ingrese el porcentaje de descuento:  "))
            self.descuentoVenta = self.montofactura - (self.montofactura * self.porcentajenew)

        return self.descuentoVenta
    
listadoFacturas = []