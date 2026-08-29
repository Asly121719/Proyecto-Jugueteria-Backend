class DetalleVenta:
    def __init__(self, id_detalle: int, id_venta: int, id_juguete: int, cantidad_comprada: int, subtotal: float):
        self.id_detalle = id_detalle
        self.id_venta = id_venta
        self.id_juguete = id_juguete
        self.cantidad_comprada = cantidad_comprada
        self.subtotal = subtotal
