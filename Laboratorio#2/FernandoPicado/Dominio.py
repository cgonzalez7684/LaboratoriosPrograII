class Factura:
    def __init__(self) -> None:
        self.idfactura = None
        self.fechafactura = None
        self.montofactura = None
        self.impuestofactura = None
        self.customer_name = None
        self.categoria_venta = None
        self.calc_desc = None

    def calculaImpuesto(self):
        self.impuestofactura = self.montofactura * 0.13
        return self.impuestofactura


listadoFacturas = []
