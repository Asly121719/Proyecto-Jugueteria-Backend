from src.database import SessionLocal
from src.entities.inventario import InventarioTienda
from src.entities.juguete import Juguete


def agregar_juguete(nombre: str, precio: float):
    db = SessionLocal()
    try:
        # El ID del juguete se autogenera solo, pero sí te pedimos categoría, proveedor y stock
        id_categoria = int(input("Ingrese el ID de la categoría: "))
        id_proveedor = int(input("Ingrese el ID del proveedor: "))
        stock_inicial = int(input("Ingrese el stock inicial para la tienda: "))
        pasillo = input("Ingrese la ubicación / pasillo (ej. Pasillo 1): ")

        # Creamos el juguete sin pasar el ID para que la base de datos lo asigne automáticamente
        nuevo_juguete = Juguete(
            nombre_producto=nombre,
            precio_unitario=precio,
            id_categoria=id_categoria,
            id_proveedor=id_proveedor,
        )
        db.add(nuevo_juguete)
        db.commit()
        db.refresh(nuevo_juguete)  # Recupera el ID autogenerado por la BD

        # Usamos ese ID automático para registrar el inventario
        nuevo_inventario = InventarioTienda(
            id_tienda=1,
            id_juguete=nuevo_juguete.id_juguete,
            stock_actual=stock_inicial,
            pasillo_ubicacion=pasillo,
        )
        db.add(nuevo_inventario)
        db.commit()

        print(
            f"\n[ÉXITO] Juguete '{nombre}' registrado con el ID automático"
            f" #{nuevo_juguete.id_juguete} (Categoría: #{id_categoria},"
            f" Proveedor: #{id_proveedor})."
        )
    except ValueError:
        print("\n[ERROR] Los IDs, precios y stock deben ser valores numéricos válidos.")
    except Exception as e:
        db.rollback()
        print(f"\n[ERROR] No se pudo agregar el juguete: {e}")
    finally:
        db.close()


def eliminar_juguete(id_juguete: int):
    db = SessionLocal()
    try:
        # Primero borramos registros de inventario asociados para evitar conflictos de llave foránea si aplica
        db.query(InventarioTienda).filter_by(id_juguete=id_juguete).delete()

        juguete = db.query(Juguete).filter_by(id_juguete=id_juguete).first()
        if not juguete:
            print(f"\n[ERROR] No se encontró un juguete con el ID {id_juguete}.")
            db.rollback()
            return

        db.delete(juguete)
        db.commit()
        print(f"\n[ÉXITO] Juguete con ID {id_juguete} eliminado correctamente.")
    except Exception as e:
        db.rollback()
        print(f"[ERROR] No se pudo eliminar el juguete: {e}")
    finally:
        db.close()


def gestionar_stock(id_juguete: int, cantidad_sumar: int, id_tienda: int = 1):
    db = SessionLocal()
    try:
        item = (
            db.query(InventarioTienda)
            .filter_by(id_juguete=id_juguete, id_tienda=id_tienda)
            .first()
        )
        if item:
            item.stock_actual += cantidad_sumar
            db.commit()
            print(
                f"\n[ÉXITO] Stock actualizado. Nuevo stock de Juguete"
                f" {id_juguete}: {item.stock_actual}"
            )
        else:
            print(
                f"\n[ALERTA] El juguete #{id_juguete} no está en el inventario de la"
                " tienda."
            )
    finally:
        db.close()


def consultar_inventario_completo():
    db = SessionLocal()
    try:
        # Hacemos un join para traer los datos reales del juguete (nombre y precio) junto al inventario
        items = (
            db.query(InventarioTienda, Juguete)
            .join(Juguete, InventarioTienda.id_juguete == Juguete.id_juguete)
            .all()
        )

        print("\n=== INVENTARIO COMPLETO DE PRODUCTOS ===")
        if not items:
            print("No hay productos registrados en el inventario.")
            return

        for item, juguete in items:
            print(
                f"ID Juguete: {juguete.id_juguete} | Producto:"
                f" {juguete.nombre_producto} | Precio: ${juguete.precio_unitario}"
                f" | Stock: {item.stock_actual} | Ubicación:"
                f" {item.pasillo_ubicacion}"
            )
    finally:
        db.close()


# Alias requerido por el main.py
def consultar_inventario():
    consultar_inventario_completo()


def reducir_stock(id_juguete: int, cantidad: int) -> bool:
    db = SessionLocal()
    try:
        item = db.query(InventarioTienda).filter_by(id_juguete=id_juguete).first()
        if item and item.stock_actual >= cantidad:
            item.stock_actual -= cantidad
            db.commit()
            return True
        return False
    finally:
        db.close()
