from entities.garantia import Garantia

garantias_db = []

def crear_garantia(id_garantia: int, id_detalle_venta: int, duracion_meses: int = 12, tipo_cobertura: str = "Defecto de fábrica"):
    nueva_garantia = Garantia(id_garantia, id_detalle_venta, duracion_meses, tipo_cobertura, "Activa")
    garantias_db.append(nueva_garantia)
    print(f"\n[ÉXITO] Garantía #{id_garantia} creada automáticamente (Estado: Activa).")
    return nueva_garantia

def consultar_garantia(id_garantia: int):
    g = next((item for item in garantias_db if item.id_garantia == id_garantia), None)
    if g:
        print(f"\n=== GARANTÍA #{g.id_garantia} ===")
        print(f"Detalle Venta ID: {g.id_detalle_venta} | Duración: {g.duracion_meses} meses")
        print(f"Cobertura: {g.tipo_cobertura} | Estado: {g.estado_garantia}")
    else:
        print(f"\n[ALERTA] No se encontró la garantía #{id_garantia}.")

def actualizar_garantia(id_garantia: int, nuevo_estado: str):
    g = next((item for item in garantias_db if item.id_garantia == id_garantia), None)
    if g:
        g.estado_garantia = nuevo_estado
        print(f"\n[ÉXITO] Garantía #{id_garantia} actualizada a estado: '{nuevo_estado}'.")
    else:
        print(f"\n[ERROR] Garantía #{id_garantia} no encontrada.")

def eliminar_garantia(id_garantia: int):
    global garantias_db
    garantias_db = [g for g in garantias_db if g.id_garantia != id_garantia]
    print(f"\n[ÉXITO] Registro de garantía #{id_garantia} eliminado correctamente.")
