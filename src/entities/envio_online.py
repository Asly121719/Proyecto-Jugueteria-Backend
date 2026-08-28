class EnvioOnline:
    def _init_(
        self,
        id_envio: int,
        id_venta: int,
        empresa_transporte: str,
        numero_guia: str,
        estado_envio: str,
    ):
        self.id_envio = id_envio
        self.id_venta = id_venta
        self.empresa_transporte = empresa_transporte
        self.numero_guia = numero_guia
        # Estados: Preparación, En Camino, Entregado
        self.estado_envio = estado_envio
