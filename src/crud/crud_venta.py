import datetime
from uuid import UUID
from src.database import SessionLocal
from src.entities.detalle_venta import DetalleVenta
from src.entities.venta import Venta

def registrar_venta(
    id_tienda: UUID,
    id_empleado: UUID,
    id_juguete: UUID,
    cantidad: int,
    precio_unitario: float,
    crud_inventario_mod,
    id_cliente: UUID = None,
):
    descuento_exitoso = crud_inventario_mod.reducir_stock(id_juguete, cantidad)
    if not descuento_exitoso:
        print("\n[ERROR] Stock insuficiente o producto no encontrado para la venta.")
        return None

    db = SessionLocal()
    try:
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        nueva_venta = Venta(
            id_tienda=id_tienda,
            id_empleado=id_empleado,
            id_cliente=id_cliente,
            fecha_hora_venta=fecha_actual,
        )
        db.add(nueva_venta)
        db.flush()

        subtotal = cantidad * precio_unitario
        nuevo_detalle = DetalleVenta(
            id_venta=nueva_venta.id_venta,
            id_juguete=id_juguete,
            cantidad_comprada=cantidad,
            subtotal=subtotal,
        )
        db.add(nuevo_detalle)
        db.commit()
        print(
            f"\n[ÉXITO] Venta #{nueva_venta.id_venta} registrada en Neon con Subtotal: ${subtotal}"
        )
        return nueva_venta
    except Exception as e:
        db.rollback()
        print(f"[ERROR] No se pudo registrar la venta: {e}")
    finally:
        db.close()

def consultar_venta(id_venta: UUID):
    db = SessionLocal()
    try:
        venta = db.query(Venta).filter_by(id_venta=id_venta).first()
        if not venta:
            print(f"\n[ALERTA] No se encontró ninguna venta con ID #{id_venta}.")
            return
        print(f"\n=== DETALLE DE VENTA #{venta.id_venta} ===")
        print(
            f"Fecha: {venta.fecha_hora_venta} | Tienda ID: {venta.id_tienda} | Empleado ID: {venta.id_empleado}"
        )
        print(f"Cliente ID: {venta.id_cliente if venta.id_cliente else 'Anónimo'}")
        print("--- Productos Comprados ---")
        for d in venta.detalles:
            print(
                f"Detalle #{d.id_detalle} -> Juguete ID: {d.id_juguete} | Cantidad: {d.cantidad_comprada} | Subtotal: ${d.subtotal}"
            )
    finally:
        db.close()