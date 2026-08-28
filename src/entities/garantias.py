class Garantia:
    def _init_(
        self,
        id_garantia: int,
        id_detalle_venta: int,
        duracion_meses: int,
        tipo_cobertura: str,
        estado_garantia: str,
    ):
        self.id_garantia = id_garantia
        self.id_detalle_venta = id_detalle_venta
        self.duracion_meses = duracion_meses
        # Coberturas: Defecto de fábrica, Daño accidental, Extendida
        self.tipo_cobertura = tipo_cobertura
        # Estados: Activa, Expirada, Reclamada
        self.estado_garantia = estado_garantia
