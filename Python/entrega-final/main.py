#Nota: Ya no importamos 'productos = [] ' ni lo pasamos como argumento
#Las funciones de 'producto' gestionan su propia conexión a la base de datos
from producto import agregar_producto, mostrar_productos, buscar_producto, eliminar_producto
from utils import mostrar_encabezado, mostrar_menu
from colorama import Fore

def menu_principal():
    
    while True:
        mostrar_encabezado()
        mostrar_menu()
        opcion = input(f"{Fore.CYAN}📥 Seleccione una opción: ").strip()

        if opcion == "1":
            #Ya no pasamos 'productos' como argumento
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
            input(f"{Fore.WHITE}Presione Enter para continuar...")
        elif opcion == "3":
            buscar_producto()
            input(f"{Fore.WHITE}Presione Enter para continuar...")
        elif opcion == "4":
            eliminar_producto()
            input(f"{Fore.WHITE}Presione Enter para continuar...")
        elif opcion == "5":
            print(f"\n{Fore.GREEN}👋 ¡Gracias por usar el sistema!")
            break
        else:
            print(f"{Fore.RED}❌ Opción inválida. Intente nuevamente.\n")
            input(f"{Fore.WHITE}Presione Enter para continuar...")

if __name__ == "__main__":
    menu_principal()    


"""
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
"""