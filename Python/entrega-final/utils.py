from colorama import init,Fore,Style    
import os

#Inicializar colorama(autoreset limpia el color al terminar el print)
init(autoreset=True)

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
def mostrar_encabezado():
    """Muestra el encabezado del sistema."""
    limpiar_pantalla()
    print(f"{Fore.CYAN}{Style.BRIGHT}=" * 50)
    print("🛒  SISTEMA DE GESTIÓN BÁSICA DE PRODUCTOS  🛒".center(50))
    print("=" * 50)

def mostrar_menu():
    """Muestra el menú principal del sistema."""
    print(f"\n{Fore.YELLOW}📦 Menú Principal")
    print(f"{Fore.WHITE}────────────────────────────")
    print(f"{Fore.GREEN}1️⃣  Agregar producto")
    print(f"{Fore.BLUE}2️⃣  Mostrar productos")  
    print(f"{Fore.MAGENTA}3️⃣  Buscar producto")
    print(f"{Fore.RED}4️⃣  Eliminar producto")  
    print(f"{Fore.WHITE}5️⃣  Salir")
    print("────────────────────────────")




"""
codigo de pre entrega
def mostrar_encabezado():
    print("=" * 50)
    print("🛒  SISTEMA DE GESTIÓN BÁSICA DE PRODUCTOS  🛒".center(50))
    print("=" * 50)

def mostrar_menu():
    print("\n📦 Menú Principal")
    print("────────────────────────────")
    print("1️⃣  Agregar producto")
    print("2️⃣  Mostrar productos")
    print("3️⃣  Buscar producto")
    print("4️⃣  Eliminar producto")
    print("5️⃣  Salir")
    print("────────────────────────────")
"""