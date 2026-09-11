import datetime
from src.database import SessionLocal
from src.entities.cargo import Cargo
from src.entities.categoria import Categoria
from src.entities.cliente import Cliente
from src.entities.detalle_venta import DetalleVenta
from src.entities.Empleado import Empleado
from src.entities.garantias import Garantia
from src.entities.inventario import InventarioTienda
from src.entities.juguete import Juguete
from src.entities.promocion import Promocion
from src.entities.Proveedor import Proveedor
from src.entities.Tienda import Tienda
from src.entities.venta import Venta


def ejecutar_seeders():
  db = SessionLocal()
  try:
    if db.query(Tienda).first():
      print("[INFO] La base de datos ya contiene datos. Omitiendo seeders.")
      return

    print("--- Ejecutando Seeders ---")

    # 1. Tienda
    t1 = Tienda(
        nombre_sucursal="Sucursal Norte",
        direccion="Calle 123 #45-67",
        telefono="3101234567",
        horario_apertura="08:00 - 20:00",
    )
    db.add(t1)
    db.flush()

    # 2. Cargo
    c1 = Cargo(
        titulo_cargo="Cajero",
        salario_base=1300000.00,
        nivel_acceso="Básico",
        funciones_principales="Atención al cliente y cobro",
    )
    db.add(c1)
    db.flush()

    # 3. Empleado
    e1 = Empleado(
        id_tienda=t1.id_tienda,
        id_cargo=c1.id_cargo,
        nombre="Ana",
        apellido="Gómez",
        correo_electronico="ana.gomez@jugueteria.com",
    )
    db.add(e1)
    db.flush()

    # 4. Categoria
    cat1 = Categoria(
        nombre_categoria="Didáctico",
        descripcion="Juguetes para estimulación temprana",
        edad_recomendada="3-6 años",
        es_electrico=False,
    )
    db.add(cat1)
    db.flush()

    # 5. Proveedor
    p1 = Proveedor(
        razon_social="Mattel S.A.",
        nombre_contacto="Carlos Perez",
        telefono="3209876543",
        pais_origen="México",
    )
    db.add(p1)
    db.flush()

    # 6. Juguete
    j1 = Juguete(
        id_categoria=cat1.id_categoria,
        id_proveedor=p1.id_proveedor,
        nombre_producto="Bloques de Madera ABC",
        precio_unitario=45000.00,
    )
    db.add(j1)
    db.flush()

    # 7. Cliente
    cli1 = Cliente(
        nombre="Pedro",
        apellido="Martínez",
        correo_electronico="pedro.m@example.com",
        telefono="3005554433",
    )
    db.add(cli1)
    db.flush()

    # 8. Inventario
    inv1 = InventarioTienda(
        id_tienda=t1.id_tienda,
        id_juguete=j1.id_juguete,
        stock_actual=50,
        pasillo_ubicacion="Pasillo 1 - Educativos",
    )
    db.add(inv1)

    # 9. Promocion
    promo1 = Promocion(
        nombre_campana="Navidad Feliz",
        porcentaje_descuento=15.0,
        fecha_inicio="2026-12-01",
        fecha_fin="2026-12-31",
    )
    promo1.juguetes.append(j1)
    db.add(promo1)

    # 10. Venta, Detalle, Envio y Garantia relacionados
    v1 = Venta(
        id_tienda=t1.id_tienda,
        id_empleado=e1.id_empleado,
        id_cliente=cli1.id_cliente,
        fecha_hora_venta=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )
    db.add(v1)
    db.flush()

    dv1 = DetalleVenta(
        id_venta=v1.id_venta,
        id_juguete=j1.id_juguete,
        cantidad_comprada=2,
        subtotal=90000.00,
    )
    db.add(dv1)
    db.flush()


    gar1 = Garantia(
        id_detalle_venta=dv1.id_detalle,
        duracion_meses=12,
        tipo_cobertura="Defecto de fábrica",
        estado_garantia="Activa",
    )
    db.add(gar1)

    db.commit()
    print("[ÉXITO] Seeders aplicados correctamente en Neon.")
  except Exception as e:
    db.rollback()
    print(f"[ERROR] Error al ejecutar seeders: {e}")
  finally:
    db.close()


if __name__ == "__main__":
  ejecutar_seeders()