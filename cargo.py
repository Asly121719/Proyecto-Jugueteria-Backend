class Cargo:
    def __init__(self, id_cargo: int, titulo_cargo: str, salario_base: float, nivel_acceso: str, funciones_principales: str):
        self.id_cargo = id_cargo
        self.titulo_cargo = titulo_cargo  # Cajero, Gerente, Asesor, etc.
        self.salario_base = salario_base
        self.nivel_acceso = nivel_acceso
        self.funciones_principales = funciones_principales
