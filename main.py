import sys
import os

# Permite resolver imports desde la carpeta raíz
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from crud import crud_venta, crud_inventario, crud_garantias

def menu_ventas():
    while True:
        print("\n--- MENÚ DE VENTAS (TRANSACCIONES) ---")
        print("1. Registrar venta")
        print("2. Consultar historial de venta")
        print("3. Volver al menú principal")
        op = input("Seleccione una opción: ")

        if op == "1":
            id_v = int(input("ID Venta: "))
            id_det = int(input("ID Detalle de Venta: "))
            id_t = int(input("ID Tienda: "))
            id_e = int(input("ID Empleado: "))
            id_j = int(input("ID Juguete a vender: "))
            cant = int(input("Cantidad a comprar: "))
            precio = float(input("Precio unitario: "))
            cli = input("ID Cliente (dejar vacío si es anónimo): ")
            id_c = int(cli) if cli.strip() else None
            
            crud_ventas.registrar_venta(id_v, id_det, id_t, id_e, id_j, cant, precio, crud_inventario, id_c)
        elif op == "2":
            id_v = int(input("Ingrese ID de Venta a buscar: "))
            crud_ventas.consultar_venta(id_v)
        elif op == "3":
            break
        else:
            print("\nOpción inválida. Intente de nuevo.")

def menu_inventario():
    while True:
        print("\n--- MENÚ DE INVENTARIO (CONTROL DE STOCK) ---")
        print("1. Ingresar/Actualizar Stock")
        print("2. Consultar Stock de un Juguete")
        print("3. Volver al menú principal")
        op = input("Seleccione una opción: ")

        if op == "1":
            id_inv = int(input("ID Inventario: "))
            id_t = int(input("ID Tienda: "))
            id_j = int(input("ID Juguete: "))
            cant = int(input("Cantidad a agregar: "))
            pasillo = input("Ubicación pasillo (opcional): ")
            crud_inventario.gestionar_stock(id_inv, id_t, id_j, cant, pasillo)
        elif op == "2":
            id_j = int(input("ID Juguete: "))
            id_t = int(input("ID Tienda: "))
            crud_inventario.consultar_stock(id_j, id_t)
        elif op == "3":
            break
        else:
            print("\nOpción inválida. Intente de nuevo.")

def menu_garantias():
    while True:
        print("\n--- MENÚ DE GARANTÍAS ---")
        print("1. Crear Garantía")
        print("2. Consultar Garantía")
        print("3. Actualizar Estado de Garantía")
        print("4. Eliminar Garantía")
        print("5. Volver al menú principal")
        op = input("Seleccione una opción: ")

        if op == "1":
            id_g = int(input("ID Garantía: "))
            id_d = int(input("ID Detalle Venta: "))
            duracion = int(input("Duración en meses (ej: 12): "))
            cobertura = input("Tipo Cobertura (Defecto de fábrica/Daño accidental/Extendida): ")
            crud_garantias.crear_garantia(id_g, id_d, duracion, cobertura)
        elif op == "2":
            id_g = int(input("ID Garantía: "))
            crud_garantias.consultar_garantia(id_g)
        elif op == "3":
            id_g = int(input("ID Garantía: "))
            estado = input("Nuevo estado (Activa/Expirada/Reclamada): ")
            crud_garantias.actualizar_garantia(id_g, estado)
        elif op == "4":
            id_g = int(input("ID Garantía a eliminar: "))
            crud_garantias.eliminar_garantia(id_g)
        elif op == "5":
            break
        else:
            print("\nOpción inválida. Intente de nuevo.")

def main():
    print("============================================")
    print("   SISTEMA DE GESTIÓN DE JUGUETERÍA v1.0   ")
    print("============================================")
    
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Módulo de Ventas")
        print("2. Módulo de Inventario")
        print("3. Módulo de Garantías")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            menu_ventas()
        elif opcion == "2":
            menu_inventario()
        elif opcion == "3":
            menu_garantias()
        elif opcion == "4":
            print("\n¡Gracias por usar el sistema! Saliendo...")
            break
        else:
            print("\nOpción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()