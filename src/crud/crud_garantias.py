from src.database import SessionLocal
from src.entities.garantias import Garantia


def crear_garantia(
    id_detalle_venta: int,
    duracion_meses: int = 12,
    tipo_cobertura: str = "Defecto de fábrica",
):
    db = SessionLocal()
    try:
        nueva_garantia = Garantia(
            id_detalle_venta=id_detalle_venta,
            duracion_meses=duracion_meses,
            tipo_cobertura=tipo_cobertura,
            estado_garantia="Activa",
        )
        db.add(nueva_garantia)
        db.commit()
        print(
            "\n[ÉXITO] Garantía creada en Neon con ID"
            f" #{nueva_garantia.id_garantia} (Estado: Activa)."
        )
        return nueva_garantia
    except Exception as e:
        db.rollback()
        print(f"[ERROR] Al crear garantía: {e}")
    finally:
        db.close()


def consultar_garantia(id_garantia: int):
    db = SessionLocal()
    try:
        g = db.query(Garantia).filter_by(id_garantia=id_garantia).first()
        if g:
            print(f"\n=== GARANTÍA #{g.id_garantia} ===")
            print(
                f"Detalle Venta ID: {g.id_detalle_venta} | Duración:"
                f" {g.duracion_meses} meses"
            )
            print(f"Cobertura: {g.tipo_cobertura} | Estado: {g.estado_garantia}")
        else:
            print(f"\n[ALERTA] No se encontró la garantía #{id_garantia}.")
    finally:
        db.close()


def actualizar_garantia(id_garantia: int, nuevo_estado: str):
    db = SessionLocal()
    try:
        g = db.query(Garantia).filter_by(id_garantia=id_garantia).first()
        if g:
            g.estado_garantia = nuevo_estado
            db.commit()
            print(
                f"\n[ÉXITO] Garantía #{id_garantia} actualizada a estado:"
                f" '{nuevo_estado}'."
            )
        else:
            print(f"\n[ERROR] Garantía #{id_garantia} no encontrada.")
    finally:
        db.close()


def eliminar_garantia(id_garantia: int):
    db = SessionLocal()
    try:
        g = db.query(Garantia).filter_by(id_garantia=id_garantia).first()
        if g:
            db.delete(g)
            db.commit()
            print(f"\n[ÉXITO] Registro de garantía #{id_garantia} eliminado de Neon.")
        else:
            print(f"\n[ERROR] Garantía #{id_garantia} no encontrada.")
    finally:
        db.close()
