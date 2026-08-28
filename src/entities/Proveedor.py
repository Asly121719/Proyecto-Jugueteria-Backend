class Proveedor:
    def _init_(
        self,
        id_proveedor: int,
        razon_social: str,
        nombre_contacto: str,
        telefono: str,
        pais_origen: str,
    ):
        self.id_proveedor = id_proveedor
        self.razon_social = razon_social
        self.nombre_contacto = nombre_contacto
        self.telefono = telefono
        self.pais_origen = pais_origen
