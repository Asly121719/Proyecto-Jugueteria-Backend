from .categoria import Categoria 

 

class Juguete: 

    def __init__(self, id_juguete: int, id_categoria: int, id_proveedor: int, nombre_producto: str, precio_unitario: float, categoria: Categoria = None): 

        self.id_juguete = id_juguete 

        self.id_categoria = id_categoria 

        self.id_proveedor = id_proveedor 

        self.nombre_producto = nombre_producto 

        self.precio_unitario = precio_unitario 

        self.categoria = categoria  # Relación con la clase Categoria 

 