from uuid import UUID
from src.database import SessionLocal
from src.entities.inventario import InventarioTienda
from src.entities.juguete import Juguete

def agregar_juguete(nombre: str, precio: float):
    db = SessionLocal()
    try:
        id_categoria = UUID(input("Ingrese el UUID de la categoría: ").strip())
        id_proveedor = UUID(input("Ingrese el UUID del proveedor: ").strip())
        id_tienda = UUID(input("Ingrese el UUID de la tienda: ").strip())
        stock_inicial = int(input("Ingrese el stock inicial para la tienda: "))
        pasillo = input("Ingrese la ubicación / pasillo (ej. Pasillo 1): ")

        nuevo_juguete = Juguete(
            nombre_producto=nombre,
            precio_unitario=precio,
            id_categoria=id_categoria,
            id_proveedor=id_proveedor,
        )
        db.add(nuevo_juguete)
        db.commit()
        db.refresh(nuevo_juguete)

        nuevo_inventario = InventarioTienda(
            id_tienda=id_tienda,
            id_juguete=nuevo_juguete.id_juguete,
            stock_actual=stock_inicial,
            pasillo_ubicacion=pasillo,
        )
        db.add(nuevo_inventario)
        db.commit()
        print(
            f"\n[ÉXITO] Juguete '{nombre}' registrado con el UUID automático #{nuevo_juguete.id_juguete}."
        )
    except ValueError:
        print("\n[ERROR] Verifique que los UUIDs ingresados sean válidos y que el stock sea un entero.")
    except Exception as e:
        db.rollback()
        print(f"\n[ERROR] No se pudo agregar el juguete: {e}")
    finally:
        db.close()

def eliminar_juguete(id_juguete: UUID):
    db = SessionLocal()
    try:
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

def gestionar_stock(id_juguete: UUID, cantidad_sumar: int, id_tienda: UUID):
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
                f"\n[ÉXITO] Stock actualizado. Nuevo stock de Juguete {id_juguete}: {item.stock_actual}"
            )
        else:
            print(f"\n[ALERTA] El juguete #{id_juguete} no está en el inventario de la tienda.")
    finally:
        db.close()

def consultar_inventario_completo():
    db = SessionLocal()
    try:
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
                f"ID Juguete: {juguete.id_juguete} | Producto: {juguete.nombre_producto} "
                f"| Precio: ${juguete.precio_unitario} | Stock: {item.stock_actual} "
                f"| Ubicación: {item.pasillo_ubicacion}"
            )
    finally:
        db.close()

def consultar_inventario():
    consultar_inventario_completo()

def reducir_stock(id_juguete: UUID, cantidad: int) -> bool:
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