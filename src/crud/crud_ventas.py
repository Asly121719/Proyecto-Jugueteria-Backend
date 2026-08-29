from entities.venta import Venta
from entities.detalle_venta import DetalleVenta
import datetime

ventas_db = []
detalles_db = []

def registrar_venta(id_venta: int, id_detalle: int, id_tienda: int, id_empleado: int, id_juguete: int, cantidad: int, precio_unitario: float, crud_inventario_mod, id_cliente: int = None):
    # 1. Verificar y descontar stock antes de crear la venta
    descuento_exitoso = crud_inventario_mod.reducir_stock(id_juguete, cantidad)
    if not descuento_exitoso:
        print("\n[ERROR] No se pudo procesar la venta. Stock insuficiente o producto no encontrado.")
        return None

    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 2. Registrar la Venta
    nueva_venta = Venta(id_venta, id_tienda, id_empleado, fecha_actual, id_cliente)
    ventas_db.append(nueva_venta)
    
    # 3. Registrar el Detalle de la Venta
    subtotal = cantidad * precio_unitario
    nuevo_detalle = DetalleVenta(id_detalle, id_venta, id_juguete, cantidad, subtotal)
    detalles_db.append(nuevo_detalle)
    
    print(f"\n[ÉXITO] Venta #{id_venta} registrada correctamente con Subtotal: ${subtotal}")
    return nueva_venta

def consultar_venta(id_venta: int):
    venta = next((v for v in ventas_db if v.id_venta == id_venta), None)
    if not venta:
        print(f"\n[ALERTA] No se encontró ninguna venta con ID #{id_venta}.")
        return
    
    detalles = [d for d in detalles_db if d.id_venta == id_venta]
    print(f"\n=== DETALLE DE VENTA #{venta.id_venta} ===")
    print(f"Fecha: {venta.fecha_hora_venta} | Tienda ID: {venta.id_tienda} | Empleado ID: {venta.id_empleado}")
    print(f"Cliente ID: {venta.id_cliente if venta.id_cliente else 'Anónimo'}")
    print("--- Productos Comprados ---")
    for d in detalles:
        print(f"Detalle #{d.id_detalle} -> Juguete ID: {d.id_juguete} | Cantidad: {d.cantidad_comprada} | Subtotal: ${d.subtotal}")