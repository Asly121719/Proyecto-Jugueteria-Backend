class Cliente:
    def __init__(self, id_cliente: int, nombre: str, apellido: str, correo_electronico: str, telefono: str):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo_electronico = correo_electronico
        self.telefono = telefono