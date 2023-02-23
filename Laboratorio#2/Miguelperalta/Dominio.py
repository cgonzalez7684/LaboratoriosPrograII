from datetime import datetime as dt

class Factura:
    def __init__(self):
        self.idfactura = None
        self.fechafactura = None        
        self.montofactura = None
        self.impuestofactura = None 
        self.nombreCliente = None
        self.categoriaVenta = None
        self.categoria = None
        self.Descuento = None
        
    def calculaImpuesto(self):
        self.impuestofactura = self.montofactura * 0.13
        return self.impuestofactura
    
    def calcularDescuento(self):
        if self.categoriaVenta == "A":
            self.Descuento = self.montofactura * 0.05
            
        elif self.categoriaVenta == "B":
            self.Descuento = self.montofactura * 0.1
            
        elif self.categoriaVenta == "C":
            montoDescuento = float(input("Ingrese el descuento: "))
            self.Descuento = montoDescuento*self.montofactura
    
            
        else:
            print("Categoría de venta no válida")

    def impresion(self):
        print("Categoria Venta:" + self.categoriaVenta 
              , "\nMonto de la factura:" , self.montofactura
              , "\nImpuesto:" , self.impuestofactura
              , "\nFecha Factura: " , self.fechafactura
              , "\nDescuento: " , self.Descuento)