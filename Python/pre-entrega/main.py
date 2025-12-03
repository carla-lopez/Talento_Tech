from producto import agregar_producto, mostrar_productos, buscar_producto, eliminar_producto
from utils import mostrar_encabezado, mostrar_menu

def menu_principal():
    productos = []

    while True:
        mostrar_encabezado()
        mostrar_menu()
        opcion = input("📥 Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_producto(productos)
        elif opcion == "2":
            mostrar_productos(productos)
        elif opcion == "3":
            buscar_producto(productos)
        elif opcion == "4":
            eliminar_producto(productos)
        elif opcion == "5":
            print("👋 ¡Gracias por usar el sistema!")
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.\n")

if __name__ == "__main__":
    menu_principal()
