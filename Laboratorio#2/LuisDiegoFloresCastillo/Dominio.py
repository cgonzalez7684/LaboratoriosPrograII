class Factura:
    def __init__(self, id_factura, nombre_cliente, categoria, fecha, monto):
        self.id_factura = id_factura
        self.nombre_cliente = nombre_cliente
        self.categoria = categoria
        self.fecha = fecha
        self.monto = monto

    def calculaImpuesto(self):
        self.impuestofactura = self.monto * 0.13
        return self.impuestofactura


listadoFacturas = []
