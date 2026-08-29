from entities.categoria import Categoria
from entities.inventario_tienda import InventarioTienda

# Creación de las 5 instancias de la clase Categoria
cat_munecos = Categoria(1, "Muñecos", "Figuras y muñecos de acción", "+3 años", False)
cat_didacticos = Categoria(
    2, "Didácticos", "Juegos para estimular el aprendizaje", "+5 años", False
)
cat_mesas = Categoria(
    3, "Juegos de Mesa", "Juegos de estrategia y destreza familiar", "+8 años", False
)
cat_carros = Categoria(
    4, "Carros y Pistas", "Vehículos a escala y pistas de carrera", "+4 años", False
)
cat_electricos = Categoria(
    5, "Electrónicos", "Juguetes interactivos con circuitos", "+6 años", True
)

# Base de datos con los 5 juguetes quemados integrando los objetos Categoria
inventario_db = [
    InventarioTienda(
        id_juguete=101,
        id_categoria=1,
        id_proveedor=501,
        nombre_producto="Muñeco de Acción",
        precio_unitario=45000.0,
        categoria=cat_munecos,
        stock_actual=20,
    ),
    InventarioTienda(
        id_juguete=102,
        id_categoria=2,
        id_proveedor=502,
        nombre_producto="Juego Didáctico Matemático",
        precio_unitario=35000.0,
        categoria=cat_didacticos,
        stock_actual=15,
    ),
    InventarioTienda(
        id_juguete=103,
        id_categoria=3,
        id_proveedor=503,
        nombre_producto="Ajedrez de Madera",
        precio_unitario=60000.0,
        categoria=cat_mesas,
        stock_actual=30,
    ),
    InventarioTienda(
        id_juguete=104,
        id_categoria=4,
        id_proveedor=504,
        nombre_producto="Carro a Control Remoto",
        precio_unitario=120000.0,
        categoria=cat_carros,
        stock_actual=12,
    ),
    InventarioTienda(
        id_juguete=105,
        id_categoria=5,
        id_proveedor=505,
        nombre_producto="Consola Portátil Infantil",
        precio_unitario=150000.0,
        categoria=cat_electricos,
        stock_actual=25,
    ),
]


def gestionar_stock(id_juguete: int, cantidad_sumar: int):
    """Actualiza el stock de un juguete existente buscando únicamente por su ID."""
    item = next((i for i in inventario_db if i.id_juguete == id_juguete), None)
    if item:
        item.stock_actual += cantidad_sumar
        print(
            f"\n[ÉXITO] Stock actualizado. Nuevo stock de '{item.nombre_producto}': {item.stock_actual} unidades."
        )
    else:
        print(
            f"\n[ALERTA] El juguete con ID #{id_juguete} no se encuentra registrado en el sistema."
        )


def consultar_inventario_completo():
    """Muestra la lista completa de todos los productos con sus atributos y stock actual."""
    if not inventario_db:
        print("\n[ALERTA] El inventario está vacío.")
        return

    print("\n--- LISTA COMPLETA DEL INVENTARIO ---")
    print(
        f"{'ID':<6} {'Nombre Producto':<28} {'Categoría':<18} {'Precio':<12} {'Stock'}"
    )
    print("-" * 75)
    for item in inventario_db:
        print(
            f"{item.id_juguete:<6} {item.nombre_producto:<28} {item.categoria.nombre_categoria:<18} ${item.precio_unitario:<11.2f} {item.stock_actual}"
        )


def reducir_stock(id_juguete: int, cantidad: int) -> bool:
    """Reduce el stock de un juguete si existe y hay disponibilidad suficiente."""
    item = next((i for i in inventario_db if i.id_juguete == id_juguete), None)
    if item and item.stock_actual >= cantidad:
        item.stock_actual -= cantidad
        return True
    return False
