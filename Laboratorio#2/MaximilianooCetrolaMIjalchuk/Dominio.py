class Factura:
    def __init__(self) -> None:
        self.idfactura = None
        self.fechafactura = None        
        self.montofactura = None
        self.impuestofactura = None 
        self.nombreCliente = None
        self.categoriaVenta = None
        self.montomasdescuento = 0 #Lugar donde se almacena el monto con el descuento
        self.descuentoopcional = 0 #variable para el despuesto opcional

    def calculaImpuesto(self):
        self.impuestofactura = self.montofactura * 0.13
        return self.impuestofactura
    
    #Metodo nuevo para el calculo del descuento
    def calculodeldescuento(self, categoria):
        if (categoria == "A")
         self.montomasdescuento = self.montofactura - (self.montofactura * 0.05)
        elif (categoria == "B")
         self.montomasdescuento = self.montofactura - (self.montofactura * 0.10)
        else:
           self.descuentoopcional - input("Digite el porcentaje del descuento;\n")
           self.montomasdescuento - self.montofactura - (self.montofactura * self.descuentoopcional)

        return self.descuentoopcional
        
listadoFacturas = []