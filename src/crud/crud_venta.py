from src.database import SessionLocal
from src.entities.detalle_venta import DetalleVenta
from src.entities.venta import Venta
import datetime


def registrar_venta(
    id_tienda: int,
    id_empleado: int,
    id_juguete: int,
    cantidad: int,
    precio_unitario: float,
    crud_inventario_mod,
    id_cliente: int = None,
):
    # 1. Verificar y reducir stock
    descuento_exitoso = crud_inventario_mod.reducir_stock(id_juguete, cantidad)
    if not descuento_exitoso:
        print("\n[ERROR] Stock insuficiente o producto no encontrado para la venta.")
        return None

    db = SessionLocal()
    try:
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 2. Registrar Cabecera de Venta
        nueva_venta = Venta(
            id_tienda=id_tienda,
            id_empleado=id_empleado,
            id_cliente=id_cliente,
            fecha_hora_venta=fecha_actual,
        )
        db.add(nueva_venta)
        db.flush()

        # 3. Registrar Detalle de Venta
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
            f"\n[ÉXITO] Venta #{nueva_venta.id_venta} registrada en Neon con"
            f" Subtotal: ${subtotal}"
        )
        return nueva_venta
    except Exception as e:
        db.rollback()
        print(f"[ERROR] No se pudo registrar la venta: {e}")
    finally:
        db.close()


def consultar_venta(id_venta: int):
    db = SessionLocal()
    try:
        venta = db.query(Venta).filter_by(id_venta=id_venta).first()
        if not venta:
            print(f"\n[ALERTA] No se encontró ninguna venta con ID #{id_venta}.")
            return

        print(f"\n=== DETALLE DE VENTA #{venta.id_venta} ===")
        print(
            f"Fecha: {venta.fecha_hora_venta} | Tienda ID: {venta.id_tienda} |"
            f" Empleado ID: {venta.id_empleado}"
        )
        print("Cliente ID:" f" {venta.id_cliente if venta.id_cliente else 'Anónimo'}")
        print("--- Productos Comprados ---")
        for d in venta.detalles:
            print(
                f"Detalle #{d.id_detalle} -> Juguete ID: {d.id_juguete} | Cantidad:"
                f" {d.cantidad_comprada} | Subtotal: ${d.subtotal}"
            )
    finally:
        db.close()
