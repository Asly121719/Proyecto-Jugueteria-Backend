from entities.inventario import InventarioTienda

inventario_db = [
    InventarioTienda(1, 1, 101, 20, "Pasillo A - Muñecos"),
    InventarioTienda(2, 1, 102, 5, "Pasillo B - Didácticos")
]

def gestionar_stock(id_inventario: int, id_tienda: int, id_juguete: int, cantidad_sumar: int, nuevo_pasillo: str = None):
    item = next((i for i in inventario_db if i.id_tienda == id_tienda and i.id_juguete == id_juguete), None)
    if item:
        item.stock_actual += cantidad_sumar
        if nuevo_pasillo:
            item.pasillo_ubicacion = nuevo_pasillo
        print(f"\n[ÉXITO] Stock actualizado. Nuevo stock de Juguete {id_juguete}: {item.stock_actual} unidades.")
    else:
        nuevo_item = InventarioTienda(id_inventario, id_tienda, id_juguete, cantidad_sumar, nuevo_pasillo or "General")
        inventario_db.append(nuevo_item)
        print(f"\n[ÉXITO] Nuevo registro de inventario creado para Juguete {id_juguete}.")

def consultar_stock(id_juguete: int, id_tienda: int):
    item = next((i for i in inventario_db if i.id_juguete == id_juguete and i.id_tienda == id_tienda), None)
    if item:
        print(f"\n[CONSULTA] Tienda #{id_tienda} | Juguete #{id_juguete} -> Disponibles: {item.stock_actual} unidades en {item.pasillo_ubicacion}")
        return item.stock_actual
    else:
        print(f"\n[ALERTA] El producto ID #{id_juguete} no se encuentra registrado en la tienda #{id_tienda}.")
        return 0

def reducir_stock(id_juguete: int, cantidad: int) -> bool:
    item = next((i for i in inventario_db if i.id_juguete == id_juguete), None)
    if item and item.stock_actual >= cantidad:
        item.stock_actual -= cantidad
        return True
    return False