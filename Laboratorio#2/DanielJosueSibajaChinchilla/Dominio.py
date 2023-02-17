class Factura:
    def __init__(self) -> None:
        self.idfactura = None
        self.fechafactura = None        
        self.montofactura = None
        self.impuestofactura = None 
        self.nombreCliente = None
        self.categoriaVenta = None
        self.monto_con_descuento = 0 #Variable para almacenar el monto con descuento
        self.porcentaje_opcional = 0 #Variable para almacenar el input del descuento personalizado
    
    def calculaImpuesto(self):
        self.impuestofactura = self.montofactura * 0.13
        return self.impuestofactura
    
    #Nuevo metodo para calcular el descuento
    def calculaDescuento(self, categoria):
        if (categoria == "A"):
            self.monto_con_descuento = self.montofactura - (self.montofactura * 0.05)
        elif (categoria == "B"):
            self.monto_con_descuento = self.montofactura - (self.montofactura * 0.10)
        else:
            self.porcentaje_opcional = input("Ingrese el porcentaje que desea aplicar de descuento:\n")
            self.monto_con_descuento = self.montofactura - (self.montofactura * self.porcentaje_opcional)

        return self.monto_con_descuento
    
listadoFacturas = []