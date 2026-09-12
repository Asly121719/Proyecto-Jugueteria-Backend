from src.models import*
import os
import sys

# Permite resolver imports desde la carpeta src
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.crud import crud_garantias, crud_inventario, crud_ventas
from src.seeders import ejecutar_seeders


def menu_ventas():
  while True:
    print("\n--- MENÚ DE VENTAS (TRANSACCIONES) ---")
    print("1. Registrar venta")
    print("2. Consultar historial de venta")
    print("3. Volver al menú principal")
    op = input("Seleccione una opción: ")
    if op == "1":
      id_t = int(input("ID Tienda (ej: 1): "))
      id_e = int(input("ID Empleado (ej: 1): "))
      id_j = int(input("ID Juguete a vender (ej: 1): "))
      cant = int(input("Cantidad a comprar: "))
      precio = float(input("Precio unitario: "))
      cli = input("ID Cliente (dejar vacío si es anónimo): ")
      id_c = int(cli) if cli.strip() else None
      crud_ventas.registrar_venta(
          id_t, id_e, id_j, cant, precio, crud_inventario, id_c
      )
    elif op == "2":
      id_v = int(input("Ingrese ID de Venta a buscar: "))
      crud_ventas.consultar_venta(id_v)
    elif op == "3":
      break
    else:
      print("\nOpción inválida. Intente de nuevo.")


def menu_inventario():
    while True:
        print("\n--- MENÚ INVENTARIO ---")
        print("1. Consultar inventario")
        print("2. Agregar nuevo juguete")
        print("3. Reducir stock")
        print("4. Eliminar juguete por ID")
        print("5. Volver al menú principal")
        op = input("Seleccione una opción: ")
        
        if op == "1":
            crud_inventario.consultar_inventario()
        elif op == "2":
            nombre = input("Nombre del juguete: ")
            precio = float(input("Precio unitario: "))
            crud_inventario.agregar_juguete(nombre, precio)
        elif op == "3":
            id_j = int(input("ID Juguete: "))
            cant = int(input("Cantidad a reducir: "))
            crud_inventario.reducir_stock(id_j, cant)
        elif op == "4":
            id_j = int(input("Ingrese el ID del juguete que desea eliminar: "))
            crud_inventario.eliminar_juguete(id_j)
        elif op == "5":
            break
        else:
            print("[ERROR] Opción no válida.")

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
      id_d = int(input("ID Detalle Venta asociado: "))
      duracion = int(input("Duración en meses (ej: 12): "))
      cobertura = input(
          "Tipo Cobertura (Defecto de fábrica/Daño accidental/Extendida): "
      )
      crud_garantias.crear_garantia(id_d, duracion, cobertura)
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
  # Ejecuta los seeders automáticamente al iniciar el sistema
  print("Inicializando conexión y seeders con Neon...")
  ejecutar_seeders()

  print("============================================")
  print("    SISTEMA DE GESTIÓN DE JUGUETERÍA v2.0    ")
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