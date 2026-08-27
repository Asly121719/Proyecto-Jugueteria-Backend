from .cargo import Cargo

class Empleado:
    def __init__(self, id_empleado: int, id_tienda: int, id_cargo: int, nombre: str, apellido: str, correo_electronico: str, cargo: Cargo = None):
        self.id_empleado = id_empleado
        self.id_tienda = id_tienda
        self.id_cargo = id_cargo
        self.nombre = nombre
        self.apellido = apellido
        self.correo_electronico = correo_electronico
        self.cargo = cargo  # Relación con la clase Cargo
