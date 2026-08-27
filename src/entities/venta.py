class Venta:
    def __init__(self, id_venta: int, id_tienda: int, id_empleado: int, fecha_hora_venta: str, id_cliente: int = None):
        self.id_venta = id_venta
        self.id_tienda = id_tienda
        self.id_cliente = id_cliente  # Puede ser None para clientes anónimos
        self.id_empleado = id_empleado
        self.fecha_hora_venta = fecha_hora_venta
