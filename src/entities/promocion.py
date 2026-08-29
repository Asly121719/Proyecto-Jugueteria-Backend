class Promocion:
    def __init__(self, id_promocion: int, nombre_campana: str, porcentaje_descuento: float, fecha_inicio: str, fecha_fin: str):
        self.id_promocion = id_promocion
        self.nombre_campana = nombre_campana
        self.porcentaje_descuento = porcentaje_descuento
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin