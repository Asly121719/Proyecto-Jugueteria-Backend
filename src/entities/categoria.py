class Categoria:
    def __init__(
        self,
        id_categoria: int,
        nombre_categoria: str,
        descripcion: str,
        edad_recomendada: str,
        es_electrico: bool,
    ):
        self.id_categoria = id_categoria
        self.nombre_categoria = (
            nombre_categoria  # ej: Didáctico, Eléctrico, Aprendizaje
        )
        self.descripcion = descripcion
        self.edad_recomendada = edad_recomendada
        self.es_electrico = es_electrico
